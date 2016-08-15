#! /usr/bin/env python3

from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView
import flask_admin as admin

'''App configuration'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'
app.config['MONGODB_SETTINGS'] = {
    'db': 'consultorio'
}

''' db init '''

db = MongoEngine()
db.init_app(app)


'''App Models'''


class Member(db.Document):
    name = db.StringField(max_lenght=20, required=True)
    last_name = db.StringField(max_lenght=20, required=True)
    birthdate = db.DateTimeField()
    email = db.EmailField()
    profile_picture = db.ImageField()
    rol = db.StringField(required=True, choices=(
                        'Actriz', 'Director', 'Tecnica'))

    def __unicode__(self):
        return self.name


class Theatre(db.Document):
    name = db.StringField(max_lenght=30, required=True)
    direction = db.StringField(max_lenght=30, required=True)
    borough = db.StringField(max_lenght=15)
    city = db.StringField(max_lenght=15)
    email = db.EmailField()

    def __unicode__(self):
        return self.name


class Genre(db.Document):
    name = db.StringField(max_lenght=15)

    def __unicode__(self):
        return self.name


class Play(db.Document):
    title = db.StringField(max_lenght=50, required=True)
    release_date = db.DateTimeField()
    genre = db.ReferenceField(Genre, required=True)
    current_theater = db.ReferenceField(Theatre, required=True)
    members = db.ListField(db.ReferenceField(Member))
    book = db.ListField(db.ReferenceField('Image'))

    def __unicode__(self):
        return self.title


# for index page configuration
class Cover(db.Document):
    '''FIXME'''
    num_images = db.IntField(required=True, max_value=3)
    images = db.ListField(db.ReferenceField('Image'), required=True)


class Image(db.Document):
    name = db.StringField(max_lenght=5)
    image = db.ImageField(required=True)

    def __unicode__(self):
        return self.name

'''Admin Views '''


class MemberView(ModelView):
    column_filters = ['name', 'rol']
    column_searcheable_list = ['name']
    column_labels = dict(
        name='Nombre',
        last_name='Apellido',
        birthdate='Fecha de Nacimiento',
        profile_picture='Foto de Perfil'
    )
    column_descriptions = dict(
        profile_picture='Imagen que se visualiza el Perfil de los integrantes'

    )
    column_editable_list = ('name', 'last_name')
    form_args = dict(
        name=dict(label='Nombre'),
        last_name=dict(label='Apellido'),
        birthdate=dict(label='Fecha de Nacimiento'),
        profile_picture=dict(label='Foto de Perfil'),
        rol=dict(label='Rol')
    )


class TheatreView(ModelView):
    column_filters = ['name']
    column_labels = dict(
        borough='Barrio',
        city='Ciudad',
        direction='Direccion',
        name='Nombre'
    )
    column_searcheable_list = ['name']
    column_editable_list = ['name']
    form_args = dict(
        borough=dict(label='Barrio'),
        city=dict(label='Ciudad'),
        direction=dict(label='Direccion'),
        name=dict(label='Nombre')
    )


class PlayView(ModelView):
    column_filters = ['title']
    column_labels = dict(
        title='Titulo',
        members='Elenco',
        release_date='Fecha de Estreno',
        current_theater='Sala Actual',
        book='Catalogo'
    )
    column_searcheable_list = ['title']
    form_args = dict(
        title=dict(label='Titulo'),
        members=dict(label='Elenco'),
        release_date=dict(label='Fecha de Estreno'),
        current_theater=dict(label='Sala Actual'),
        book=dict(label='Catalogo')
    )
    column_descriptions = dict(
        book='Catalogo de imagenes'
    )


class GenreView(ModelView):
    column_filters = ['name']
    column_labels = dict(name='Genero')
    form_args = dict(
        genre=dict(label='Genero')
    )


class CoverView(ModelView):
    pass


class ImageView(ModelView):
    column_labels = dict(
        name='Nombre',
        image='Imagen'
    )
    form_args = dict(
        name=dict(label='Nombre'),
        image=dict(label='Imagen')
    )


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

    '''App Run'''
    app.run(debug=True)
