from flask import Flask
from flask_mongoengine import MongoEngine
from flask_babelex import Babel


'''App configuration'''

app = Flask(__name__)

from consultorioWeb import views

babel = Babel(app)
app.config['SECRET_KEY'] = '1234567890'
app.config['MONGODB_SETTINGS'] = {
    'db': 'consultorio'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'es'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'America/Argentina/Cordoba'

''' db init '''

db = MongoEngine()
db.init_app(app)

'''Admi needs'''
from consultorioWeb.views import *
from consultorioWeb.admin import *
import flask_admin as admin


'''Create admin'''
admin = admin.Admin(
    app,
    'Consultorio Teatro Admin'
)

admin.add_view(MemberView(Member, name='Integrantes'))
admin.add_view(TheatreView(Theatre, name='Salas'))
admin.add_view(PlayView(Play, name='Obras'))
admin.add_view(GenreView(Genre, name='Generos'))
admin.add_view(CoverView(Cover, name='Configuracion de Portada'))
admin.add_view(ImageView(Image, name='Imagenes'))
