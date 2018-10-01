from flask_wtf import Form
from wtforms import StringField, SubmitField, FloatField, SelectField
from wtforms.validators import Required
from diplom.altenergy.fluidlist.fluidlist import FluidList

fluidlist = FluidList()
paramList = FluidList()

class FluidInformationForm(Form):
    fluid = SelectField("Выбрать вещество", choices=fluidlist.get_special_fluids())
    submit = SubmitField('Получить информацию о веществе')
