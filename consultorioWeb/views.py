from consultorioWeb import app
from flask import render_template

'''App Views'''


@app.route('/')
def index():
    return render_template('base_index.html')


@app.route('/nosotros')
def about():
    return render_template('base_about.html')


@app.route('/obras')
def obras():
    return render_template('base_portfolio.html')


@app.route('/contacto')
def contact():
    return render_template('base_contacto.html')
