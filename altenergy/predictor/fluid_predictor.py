from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string
import CoolProp.CoolProp as CoolProp
from CoolProp.HumidAirProp import HAPropsSI
from diplom.altenergy.fluidlist.fluidlist import FluidList
from diplom.altenergy.fluidinfo.fluidinfo import FluidInfo

# Список веществ
fluidlist = FluidList()
fluids = fluidlist.get_all_fluids()

class Predictor:
    """ class for Predict optimal work fluid """
    def predict_fluid(self, tempHotInput:float, tempHotInputUnit:str, tempHotOutput:float, tempHotOutputUnit:str, fluid_list):
        # Температура конденсации ˚C
        tempCond = 40
        # предиктор
        predictor = 0
        # Массив для хранения результата
        listResult = []
        # итератор
        i = 1

        fluidinfo = FluidInfo()

        # Проверка единиц измерения температуры
        if tempHotInputUnit == 'K':
            tempHotInput = tempHotInput - 273.15
        if tempHotOutputUnit == 'K':
            tempHotOutput = tempHotOutput - 273.15

        # Начальная температура испарения
        tEvaporation = 0.0
        tEvaporation = tempHotInput - 15.0

        while True:
            for fluid in fluid_list:
                # Критическая температура
                tCrit = round(fluidinfo.getCritTemp(fluid, 3), 3)

                # Давление рабочего тела перед насосом
                try:
                    p2 = round(PropsSI('P', 'T', (tempCond + 273.15), 'Q', 0, fluid)/100000, 3)
                except:
                    p2 = 'не считается'
                    # one_result_list = (i, fluid, tEvaporation, tCrit, p2, '-+-', '-+-', '-+-', '-+-', '-+-', '-+-', '-+-')
                    # listResult.append(one_result_list)
                    # i += 1
                    continue

                if tCrit < tEvaporation or p2 < 1.0:
                    # one_result_list = (i, fluid, tEvaporation, tCrit, p2, '---', '---', '---', '---', '---', '---', '---')
                    # listResult.append(one_result_list)
                    # i += 1
                    continue
                else:
                    try:
                        # Энтальпия насыщенной жидкости при подогреве
                        hx0 = round(PropsSI('H', 'T', (tEvaporation + 273.15), 'Q', 0, fluid)/1000, 3)

                        # Энтальпия насыщенного пара при подогреве
                        h3 = round(PropsSI('H', 'T', (tEvaporation + 273.15), 'Q', 1, fluid)/1000, 3)

                        # Давление рабочего тела после насоса
                        p1 = round(PropsSI('P', 'T', (tEvaporation + 273.15), 'Q', 0, fluid)/100000, 3)

                        # Энтальпия конденсации
                        hcond = round(PropsSI('H', 'T', (tempCond + 273.15), 'Q', 0, fluid)/1000, 3)

                        # Давление рабочего тела перед насосом
                        p2 = round(PropsSI('P', 'T', (tempCond + 273.15), 'Q', 0, fluid)/100000, 3)

                        # Энтальпия после насоса
                        h2 = hcond

                        # Теплота парообразования
                        rl = round(h3 - hx0, 3)

                        # Теплота подогрева рабочего тела
                        rs = round(hx0 - h2, 3)

                        # Предиктор
                        predictor = self.get_predictor(tempHotInput, tEvaporation, rs, rl, tempCond)
                    except:
                        print('i=', i, predictor)

                one_result_list = (i, fluid, tEvaporation, tCrit, p2, hx0, h3, p1, hcond, rs, rl, predictor)
                listResult.append(one_result_list)
                i += 1

                if predictor >= 0.0:
                    break
            if predictor >= 0.0:
                break
            tEvaporation -= 1

        # print(fluid, tEvaporation, predictor)
        return listResult


    def get_predictor(self, tempHotInput, tEvaporation, rs, rl, tempCond):
        """ get predictor's value """
        predictor = (tempHotInput - (tEvaporation + 10)) * rl / rs - (tEvaporation - tempCond)
        return round(predictor, 3)















class PointParams:
    """
        class for getting parameters in points

        1 - point after condenser
        2 - point after pump
        3 - point before turbine
        4 - point after turbine
    """
    def get_params_point_1(self, tempHotInput, tempHotInputUnit):
        """ this function allow to get temperature, pressure, enthalpy in point 1 """
        if tempHotInputUnit == '˚C':
            tempHotInputUnit = tempHotInputUnit - 273,15
        t1 = tempHotInput - 10
        h1 = 4

    def get_params_point_2(self, ):
        """ this function allow to get temperature, pressure, enthalpy in point 2 """


    def get_params_point_3(self, ):
        """ this function allow to get temperature, pressure, enthalpy in point 3 """


    def get_params_point_4(self, ):
        """ this function allow to get temperature, pressure, enthalpy in point 4 """
