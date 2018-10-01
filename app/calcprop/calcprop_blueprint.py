from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from . forms import CalcPropForm
from diplom.altenergy.fluidlist.fluidlist import FluidList
from diplom.altenergy.calcprop.calcprop import CalcProp

calcprop_blueprint = Blueprint('calcprop_blueprint', __name__, template_folder='templates')


@calcprop_blueprint.route('/', methods=['GET', 'POST'])
def calculate_prop():
    fluidlist = FluidList()
    form = CalcPropForm()
    calcprop = CalcProp()

    if form.validate_on_submit():
        session['current_fluid'] = form.current_fluid.data
        session['inputFirstParam'] = form.inputFirstParam.data
        session['inputFirstParamNumber'] = form.inputFirstParamNumber.data
        session['inputSecondParam'] = form.inputSecondParam.data
        session['inputSecondParamNumber'] = form.inputSecondParamNumber.data

        return redirect(url_for('calcprop_blueprint.calculate_prop'))


    calcPropObject = calcprop.find_func(session.get('current_fluid'),
                       session.get('inputFirstParam'),
                       session.get('inputFirstParamNumber'),
                       session.get('inputSecondParam'),
                       session.get('inputSecondParamNumber'))



    return render_template('calcprop.html',
                           prop_form=form,
                           calcPropObject=calcPropObject,
                           current_fluid = session.get('current_fluid'),
                           fluid_dict = dict(fluidlist.get_special_fluids()))
