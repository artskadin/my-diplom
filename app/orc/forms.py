from flask_wtf import Form
from wtforms import StringField, SubmitField, FloatField, SelectField, SelectMultipleField
from wtforms.validators import Required
from diplom.altenergy.fluidlist.fluidlist import FluidList

fluidlist = FluidList()


class CalcCycleForm(Form):
    selected_fluids_list = SelectMultipleField("Выбрать вещества", choices=fluidlist.get_special_fluids())
    inputTempIn = FloatField('Введите температуру на входе')
    inputTempInUnit = SelectField('Ед изм', choices=[('˚C', '˚C'), ('K', 'K')])
    inputTempOut = FloatField('Введите температуру на выходе')
    inputTempOutUnit = SelectField('Ед изм', choices=[('˚C', '˚C'), ('K', 'K')])
    # inputHotWaterConsumption = FloatField('Введите расход')
    # inputHotWaterConsumptionUnit = SelectField('Ед изм', choices=[('кг/с', 'кг/c'), ('кг/мин', 'кг/мин')])
    # inputTurbineEfficiency = FloatField('Введите КПД турбины')
    # inputPumpEfficiency = FloatField('Введите КПД насоса')
    # inputCoolWaterIn = FloatField('Введите температуру охл.воды на входе')
    # inputCoolWaterInUnit = SelectField('Ед изм', choices=[('˚C', '˚C'), ('K', 'K')])
    # inputCoolWaterOut = FloatField('Введите температуру охл.воды на выходе')
    # inputCoolWaterOutUnit = SelectField('Ед изм', choices=[('˚C', '˚C'), ('K', 'K')])
    
    submit = SubmitField('Произвести расчет')
