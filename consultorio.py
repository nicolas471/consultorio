from flask import Flask, render_template
from flask_mongoengine import MongoEngine

'''App configuration'''
db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'consultorio'
}
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


class Theatre(db.Document):
    name = db.StringField(max_lenght=30, required=True)
    direction = db.StringField(max_lenght=30, required=True)
    borough = db.StringField(max_lenght=15)
    city = db.StringField(max_lenght=15)
    email = db.EmailField()


class Genre(db.Document):
    name = db.StringField(max_lenght=15)


class Play(db.Document):
    title = db.StringField(max_lenght=50, required=True)
    release_date = db.DateTimeField()
    genre = db.ReferenceField(Genre, required=True)
    current_theater = db.ReferenceField(Theatre, required=True)
    members = db.ListField(db.ReferenceField(Member))
    book = db.ListField(db.ImageField())


# for index page configuration
class Cover(db.Document):
    num_images = db.IntField(required=True, max_value=3)
    images = db.ListField(db.ImageField(), required=True)

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
