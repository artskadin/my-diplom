from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string
import CoolProp.CoolProp as CoolProp
from CoolProp.HumidAirProp import HAPropsSI

class CalcProp:
    def find_func(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ this function finds sytisfying condition by first and second parameters. """
        if fp == 'P' and sp == 'T' or fp == 'T' and sp == 'P':
            pt = PT()
            aprops = AnotherProps()
            d = str(pt.dpt(fluid, fp, fpv, sp, spv))
            v = str(pt.vpt(fluid, fp, fpv, sp, spv))
            h = str(pt.hpt(fluid, fp, fpv, sp, spv)/1000)
            s = str(pt.spt(fluid, fp, fpv, sp, spv)/1000)
            x = str(pt.xpt(fluid, fp, fpv, sp, spv))
            phase = str(aprops.get_phase(fluid, fp, fpv, sp, spv))
            conductivity = str(aprops.get_thermal_conductivity(fluid, fp, fpv, sp, spv))
            viscosity = str(aprops.get_dynamic_viscosity(fluid, fp, fpv, sp, spv))
            speed_of_sound = str(aprops.get_sound_of_speed(fluid, fp, fpv, sp, spv))
            prandtl = str(aprops.get_prandtl(fluid, fp, fpv, sp, spv))
            cp = str(aprops.get_cp(fluid, fp, fpv, sp, spv)/1000)
            cv = str(aprops.get_cv(fluid, fp, fpv, sp, spv)/1000)
            fpv = str(fpv)
            spv = str(spv)
            p = fpv if fp == 'P' else spv
            t = spv if sp == 'T' else fpv

            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x,
                           'phase': phase,
                           'conductivity': conductivity,
                           'viscosity': viscosity,
                           'speed_of_sound': speed_of_sound,
                           'prandtl': prandtl,
                           'cp': cp,
                           'cv': cv}
            return list_result
        elif fp == 'P' and sp == 'D' or fp == 'D' and sp == 'P':
            pd = PD()
            t = str(pd.tpd(fluid, fp, fpv, sp, spv))
            v = str(pd.vpd(fluid, fp, fpv, sp, spv))
            h = str(pd.hpd(fluid, fp, fpv, sp, spv))
            s = str(pd.spd(fluid, fp, fpv, sp, spv))
            x = str(pd.xpd(fluid, fp, fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            p = fpv if fp == 'P' else spv
            d = spv if sp == 'D' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'P' and sp == 'V' or fp == 'V' and sp == 'P':
            pass
            # Пока не знаю как реализовать
        elif fp == 'P' and sp == 'H' or fp == 'H' and sp == 'P':
            ph = PH()
            t = str(ph.tph(fluid, fp, fpv, sp, spv))
            d = str(ph.dph(fluid, fp, fpv, sp, spv))
            v = str(ph.vph(fluid, fp, fpv, sp, spv))
            s = str(ph.sph(fluid, fp, fpv, sp, spv))
            x = str(ph.xph(fluid, fp, fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            p = fpv if fp == 'P' else spv
            h = spv if sp == 'H' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'P' and sp == 'S' or fp == 'S' and sp == 'P':
            ps = PS()
            t = str(ps.tps(fluid, fp, fpv, sp, spv))
            d = str(ps.dps(fluid, fp, fpv, sp, spv))
            v = str(ps.vps(fluid, fp, fpv, sp, spv))
            h = str(ps.hps(fluid, fp, fpv, sp, spv))
            x = str(ps.xps(fluid, fp, fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            p = fpv if fp == 'P' else spv
            s = spv if sp == 'S' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'P' and sp == 'Q' or fp == 'Q' and sp == 'P':
            px = PQ()
            t = str(px.tpx(fluid, fp ,fpv, sp, spv))
            d = str(px.dpx(fluid, fp ,fpv, sp, spv))
            v = str(px.vpx(fluid, fp ,fpv, sp, spv))
            h = str(px.hpx(fluid, fp ,fpv, sp, spv))
            s = str(px.spx(fluid, fp ,fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            p = fpv if fp == 'P' else spv
            x = spv if sp == 'Q' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'T' and sp == 'D' or fp == 'D' and sp == 'T':
            td = TD()
            p = str(td.ptd(fluid, fp, fpv, sp, spv))
            v = str(td.vtd(fluid, fp, fpv, sp, spv))
            h = str(td.htd(fluid, fp, fpv, sp, spv))
            s = str(td.std(fluid, fp, fpv, sp, spv))
            x = str(td.xtd(fluid, fp, fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            t = fpv if fp == 'T' else spv
            d = spv if sp == 'D' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'T' and sp == 'V' or fp == 'V' and sp == 'T':
            pass
            # Пока пусто
        elif fp == 'T' and sp == 'S' or fp == 'S' and sp == 'T':
            ts = TS()
            p = str(ts.pts(fluid, fp ,fpv, sp, spv))
            d = str(ts.dts(fluid, fp ,fpv, sp, spv))
            v = str(ts.vts(fluid, fp ,fpv, sp, spv))
            h = str(ts.hts(fluid, fp ,fpv, sp, spv))
            x = str(ts.xts(fluid, fp ,fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            t = fpv if fp == 'T' else spv
            s = spv if sp == 'S' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result
        elif fp == 'T' and sp == 'Q' or fp == 'Q' and sp == 'T':
            tx = TQ()
            p = str(tx.ptx(fluid, fp, fpv, sp, spv))
            d = str(tx.dtx(fluid, fp, fpv, sp, spv))
            v = str(tx.vtx(fluid, fp, fpv, sp, spv))
            h = str(tx.htx(fluid, fp, fpv, sp, spv))
            s = str(tx.stx(fluid, fp, fpv, sp, spv))
            fpv = str(fpv)
            spv = str(spv)
            t = fpv if fp == 'T' else spv
            x = spv if sp == 'Q' else fpv
            list_result = {'pressure': p,
                           'temperature': t,
                           'enthalpy': h,
                           'entropy': s,
                           'volume': v,
                           'density': d,
                           'quality': x}
            return list_result


class PT:
    """ class for obtaining parameter values by pressure and temperature.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def dpt(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by pressure and temperature"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dpt does not work'
        return result

    def vpt(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by pressure and temperature"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = round((1 / result), n)
        except:
            result = 'vpt does not work'
        return result

    def hpt(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by pressure and temperature"""
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'hpt does not work'
        return result

    def spt(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by pressure and temperature"""
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'spt does not work'
        return result

    def xpt(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by pressure and temperature"""
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xpt does not work'
        return result


class PD:
    """ class for obtaining parameter values by pressure and density.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def tpd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get temperature by pressure and density"""
        try:
            result = round(PropsSI('T', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'tpd does not work'
        return result

    def vpd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by pressure and density"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vpd does not work'
        return result

    def hpd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by pressure and density"""
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'hpd does not work'
        return result

    def spd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by pressure and density"""
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'spd does not work'
        return result

    def xpd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by pressure and density"""
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xpd does not work'
        return result


class PV(PD):
    """ class for obtaining parameter values by pressure and volume.
        PropsSI function can not calculate by volume.
        By this reason volume changes by density and PV extends PD.
    """
    def getDensity(self, volume):
        try:
            density = 1 / volume
        except:
            result = 'density has not found'
            print(result)
        return result


class PH:
    """ class for obtaining parameter values by pressure and enthalpy.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def tph(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get temperature by pressure and enthalpy"""
        try:
            result = round(PropsSI('T', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'tph does not work'
        return result

    def dph(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by pressure and enthalpy"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dph does not work'
        return result

    def vph(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by pressure and enthalpy"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vph does not work'
        return result

    def sph(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by pressure and enthalpy"""
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'sph does not work'
        return result

    def xph(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by pressure and enthalpy"""
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xph does not work'
        return result


class PS:
    """ class for obtaining parameter values by pressure and enthropy.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def tps(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get temperature by pressure and entropy"""
        try:
            result = round(PropsSI('T', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'tps does not work'
        return result

    def dps(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by pressure and entropy"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dps does not work'
        return result

    def vps(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by pressure and entropy"""
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vps does not work'
        return result

    def hps(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by pressure and entropy"""
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'hps does not work'
        return result

    def xps(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by pressure and entropy"""
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xps does not work'
        return result


class PQ:
    """ class for obtaining parameter values by pressure and vapor quality.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def tpx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get temperature by pressure and vapor quality """
        try:
            result = round(PropsSI('T', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'tpx does not work'
        return result

    def dpx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by pressure and vapor quality """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dpx does not work'
        return result

    def vpx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by pressure and vapor quality """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vpx does not work'
        return result

    def hpx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by pressure and vapor quality """
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'hpx does not work'
        return result

    def spx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by pressure and vapor quality """
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'spx does not work'
        return result


class TD:
    """ class for obtaining parameter values by temperature and density.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def ptd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get pressure by temperature and density """
        try:
            result = round(PropsSI('P', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'ptd does not work'
        return result

    def vtd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        pass
        # jdfjfsjsflsjdfkjsdkfjhsdlhfgsdjhgflsdjhfljshdfjhsd

    def htd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by temperature and density """
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'htd does not work'
        return result

    def std(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by temperature and density """
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'std does not work'
        return result

    def xtd(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by temperature and density """
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xtd does not work'
        return result


class TV(TD):
    """ class for obtaining parameter values by temperature and volume.
        PropsSI function can not calculate by volume.
        By this reason volume changes by density and TV extends TD.
    """
    def getDensity(self, volume):
        try:
            density = 1 / volume
        except:
            result = 'density has not found'
            print(result)
        return result


class TS:
    """ class for obtaining parameter values by temperature and enthropy.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def pts(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get pressure by temperature and entropy """
        try:
            result = round(PropsSI('P', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'pts does not work'
        return result

    def dts(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by temperature and entropy """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dts does not work'
        return result

    def vts(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by temperature and entropy """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vts does not work'
        return result

    def hts(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by temperature and entropy """
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'hts does not work'
        return result

    def xts(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get vapor quality by temperature and entropy """
        try:
            result = round(PropsSI('Q', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'xts does not work'
        return result


class TQ:
    """ class for obtaining parameter values by temperature and vapor quality.
        fluid - work fluid,
        fp - first parameter,
        fpv - first parameter value,
        sp - second parameter,
        spv - second parameter value.
    """
    def ptx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get pressure by temperature and vapor quality """
        try:
            result = round(PropsSI('P', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'ptx does not work'
        return result

    def dtx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get density by temperature and vapor quality """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'dtx does not work'
        return result

    def vtx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get volume by temperature and vapor quality """
        try:
            result = round(PropsSI('D', fp, fpv, sp, spv, fluid), n)
            result = 1 / result
        except:
            result = 'vtx does not work'
        return result

    def htx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get enthalpy by temperature and vapor quality """
        try:
            result = round(PropsSI('H', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'htx does not work'
        return result

    def stx(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get entropy by temperature and vapor quality """
        try:
            result = round(PropsSI('S', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'stx does not work'
        return result


class AnotherProps:
    """ class for obtaining properties:
        fluid's phase,
        thermal conductivity,
        dynaic viscosity,
        speed of sound,
        prandtl number,
        Cp,
        Cv
    """
    def get_phase(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get fluid's phase """
        try:
            result = PhaseSI(fp, fpv, sp, spv, fluid)
        except:
            result = 'phase does not work'
        return result

    def get_thermal_conductivity(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get value of thermal conductivity """
        try:
            result = round(PropsSI('conductivity', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'conductivity does not work'
        return result

    def get_dynamic_viscosity(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=8):
        """ get value of dynaic viscosity """
        try:
            result = round(PropsSI('viscosity', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'viscosity does not work'
        return result

    def get_sound_of_speed(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get value of speed of sound """
        try:
            result = round(PropsSI('speed_of_sound', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'speed of sound does not work'
        return result

    def get_prandtl(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get value of prandtl number """
        try:
            result = round(PropsSI('Prandtl', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'Prandtl does not work'
        return result

    def get_cp(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get value of pressure specific heat """
        try:
            result = round(PropsSI('Cpmass', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'Cpmass does not work'
        return result

    def get_cv(self, fluid:str, fp:str, fpv:float, sp:str, spv:float, n:int=4):
        """ get value of volume specific heat """
        try:
            result = round(PropsSI('Cvmass', fp, fpv, sp, spv, fluid), n)
        except:
            result = 'Cvmass does not work'
        return result
