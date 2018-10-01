from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string
import CoolProp.CoolProp as CoolProp
from CoolProp.HumidAirProp import HAPropsSI


class FluidInfo:
    def getCritPressure(self, fluid, n):
        """ давление в критической точке """
        try:
            result = round(PropsSI(fluid, 'pcrit')/100000, n)
        except:
            result = 'нет значения'
        return result


    def getCritTemp(self, fluid, n):
        """ температура в критической точке """
        try:
            result = round(PropsSI(fluid, 'Tcrit')-273.15, n)
        except:
            result = 'нет значения'
        return result


    def getCritDensity(self, fluid, n):
        """ плотность в критической точке """
        try:
            result = round(PropsSI(fluid, 'rhocrit'), n)
        except:
            result = 'нет значения'
        return result


    def getLimitMinPressure(self, fluid, n):
        """ минимальное давление (граничные параметры) """
        try:
            result = round(PropsSI(fluid, 'pmin')/100000, n)
        except:
            result = 'нет значения'
        return result


    def getLimitMaxPressure(self, fluid, n):
        """ максимальное давление (граничные параметры) """
        try:
            result = round(PropsSI(fluid, 'pmax')/100000, n)
        except:
            result = 'нет значения'
        return result


    def getLimitMinTemp(self, fluid, n):
        """ минимальная температура (граничные параметры) """
        try:
            result = round(PropsSI(fluid, 'Tmin')-273.15, n)
        except:
            result = 'нет значения'
        return result


    def getLimitMaxTemp(self, fluid, n):
        """ максимальная температура (граничные параметры) """
        try:
            result = round(PropsSI(fluid, 'Tmax')-273.15, n)
        except:
            result = 'нет значения'
        return result


    def getMolarMass(self, fluid, n):
        """ молярная масса """
        try:
            result = round(PropsSI(fluid, 'molar_mass'), n)
        except:
            result = 'нет значения'
        return result


    def getGWP20(self, fluid, n):
        """ потенциал глобального потепления на 20 лет """
        try:
            result = round(PropsSI(fluid, 'GWP20'), n)
        except:
            result = 'нет значения'
        return result


    def getGWP100(self, fluid, n):
        """ потенциал глобального потепления на 100 лет """
        try:
            result = round(PropsSI(fluid, 'GWP100'), n)
        except:
            result = 'нет значения'
        return result


    def getGWP500(self, fluid, n):
        """ потенциал глобального потепления на 500 лет """
        try:
            result = round(PropsSI(fluid, 'GWP500'), n)
        except:
            result = 'нет значения'
        return result


    def getFlammabilityHazard(self, fluid, n):
        """ класс взрывоопасности """
        try:
            result = round(PropsSI(fluid, 'FH'), n)
        except:
            result = 'нет значения'
        return result
