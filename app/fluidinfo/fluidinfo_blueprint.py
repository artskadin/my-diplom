from flask import Blueprint, render_template, request, redirect, url_for, session
from . forms import FluidInformationForm
from diplom.altenergy.fluidlist.fluidlist import FluidList
from diplom.altenergy.fluidinfo.fluidinfo import FluidInfo

fluid_info_blueprint = Blueprint('fluid_info_blueprint', __name__, template_folder='templates')

@fluid_info_blueprint.route('/', methods=['GET', 'POST'])
def get_info():
    fluidlist = FluidList()
    fluidinfo = FluidInfo()
    form = FluidInformationForm()
    if form.validate_on_submit():
        session['fluid'] = form.fluid.data

        return redirect(url_for('fluid_info_blueprint.get_info'))
    return render_template('fluidinfo.html', fluid_info_form=form,
                                            fluid = session.get('fluid'),
                                            fluidlist = fluidlist.get_special_fluids(),
                                            fluid_dict = dict(fluidlist.get_special_fluids()),
                                            critPressure = fluidinfo.getCritPressure(session.get('fluid'), 4),
                                            critTemperature = fluidinfo.getCritTemp(session.get('fluid'), 4),
                                            critDensity = fluidinfo.getCritDensity(session.get('fluid'), 4),
                                            minPressure = fluidinfo.getLimitMinPressure(session.get('fluid'), 4),
                                            maxPressure = fluidinfo.getLimitMaxPressure(session.get('fluid'), 4),
                                            minTemperature = fluidinfo.getLimitMinTemp(session.get('fluid'), 4),
                                            maxTemperature = fluidinfo.getLimitMaxTemp(session.get('fluid'), 4),
                                            molarMass = fluidinfo.getMolarMass(session.get('fluid'), 4),
                                            gwp20 = fluidinfo.getGWP20(session.get('fluid'), 4),
                                            gwp100 = fluidinfo.getGWP100(session.get('fluid'), 4),
                                            gwp500 = fluidinfo.getGWP500(session.get('fluid'), 4),
                                            flammabilirtHazard= fluidinfo.getFlammabilityHazard(session.get('fluid'), 4))
