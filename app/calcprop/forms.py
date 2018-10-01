from flask_wtf import Form
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import Required, NumberRange
from diplom.altenergy.fluidlist.fluidlist import FluidList

fluidlist = FluidList()
paramList = FluidList()


class CalcPropForm(Form):
    current_fluid = SelectField("Выбрать вещество", choices=fluidlist.get_special_fluids())
    # характеристики первого параметра
    inputFirstParam = SelectField("Выберите параметр", choices=paramList.getParamList())
    inputFirstParamNumber = FloatField('Введите число')
    inputFirstParamUnit = SelectField('Ед изм', choices=[('Па', 'Па')])
    # характеристики второго параметра
    inputSecondParam = SelectField('Выберите параметр', choices=paramList.getParamList())
    inputSecondParamNumber = FloatField('Введите число')
    inputSecondParamUnit = SelectField('Ед изм', choices=[('K', 'K')])

    submit = SubmitField('Посчитать')
