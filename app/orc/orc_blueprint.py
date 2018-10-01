from flask import Blueprint, render_template, request, redirect, url_for, session
from .forms import CalcCycleForm
from diplom.altenergy.fluidlist.fluidlist import FluidList
from diplom.altenergy.predictor.fluid_predictor import Predictor


orc_blueprint = Blueprint('orc_blueprint', __name__, template_folder='templates')

@orc_blueprint.route('/', methods=['GET', 'POST'])
def get_orc():
    # Список веществ
    fluidlist = FluidList()
    fluids = fluidlist.get_all_fluids()


    form = CalcCycleForm()
    predictor = Predictor()


    if form.validate_on_submit():
        session['inputTempIn'] = form.inputTempIn.data
        session['inputTempInUnit'] = form.inputTempInUnit.data
        session['inputTempOut'] = form.inputTempOut.data
        session['inputTempOutUnit'] = form.inputTempOutUnit.data
        # session['inputHotWaterConsumption'] = form.inputHotWaterConsumption.data
        # session['inputTurbineEfficiency'] = form.inputTurbineEfficiency.data
        # session['inputPumpEfficiency'] = form.inputPumpEfficiency.data
        # session['inputCoolWaterIn'] = form.inputCoolWaterIn.data
        # session['inputCoolWaterOut'] = form.inputCoolWaterOut.data
        session['selected_fluids_list'] = form.selected_fluids_list.data

        return redirect(url_for('orc_blueprint.get_orc'))


    predictor_of_all_fluids = predictor.predict_fluid(
                            session.get('inputTempIn'),
                            session.get('inputTempInUnit'),
                            session.get('inputTempOut'),
                            session.get('inputTempOutUnit'),
                            fluids)


    predictor_of_certain_fluids = predictor.predict_fluid(
                            session.get('inputTempIn'),
                            session.get('inputTempInUnit'),
                            session.get('inputTempOut'),
                            session.get('inputTempOutUnit'),
                            session.get('selected_fluids_list'))

    return render_template('orc.html',
                           orc_form=form,
                           predictor1=predictor_of_all_fluids,
                           predictor2=predictor_of_certain_fluids)
