from consultorioWeb import db


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
        return '{0} {1}'.format(self.name, self.last_name)


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