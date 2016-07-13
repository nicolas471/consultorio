from flask import Flask, render_template
from flask_mongoengine import MongoEngine

'''App configuration'''
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'consultorio'
}
db = MongoEngine(app)


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

if __name__ == '__main__':
    app.run()
