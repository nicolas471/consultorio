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
    book = db.ListField(db.ImageField())

    def __unicode__(self):
        return self.title


# for index page configuration
class Cover(db.Document):
    num_images = db.IntField(required=True, max_value=3)
    images = db.ListField(db.ImageField(), required=True)


'''Admin Views TODO'''


class MemberView(ModelView):
    column_filters = ['name']


class TheatreView(ModelView):
    column_filters = ['name']


class PlayView(ModelView):
    column_filters= ['title']


class GenreView(ModelView):
    column_filters = ['name']


class CoverView(ModelView):
    pass


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
    admin = admin.Admin(app, 'Consultorio Teatro')

    '''Add Views TODO'''
    admin.add_view(MemberView(Member))
    admin.add_view(TheatreView(Theatre))
    admin.add_view(PlayView(Play))
    admin.add_view(GenreView(Genre))
    admin.add_view(CoverView(Cover))

    '''App Run'''
    app.run(debug=True)
