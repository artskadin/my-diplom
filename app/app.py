from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from diplom.app.calcprop.calcprop_blueprint import calcprop_blueprint
from diplom.app.fluidinfo.fluidinfo_blueprint import fluid_info_blueprint
from diplom.app.orc.orc_blueprint import orc_blueprint


app = Flask(__name__)

app.register_blueprint(calcprop_blueprint, url_prefix='/calcprop')
app.register_blueprint(fluid_info_blueprint, url_prefix='/fluid_info')
app.register_blueprint(orc_blueprint, url_prefix='/orc')


bootstrap = Bootstrap(app)


app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__== "__main__":
    app.run()
