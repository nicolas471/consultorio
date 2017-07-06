from django.db import models


class Member(models.Model):
    name = models.CharField(max_lenght=20, required=True)
    last_name = models.CharField(max_lenght=20, required=True)
    birthdate = models.DateTimeField()
    email = models.EmailField()
    profile_picture = models.ForeignKey('Image')
    rol = models.ForeignKey('Rol')

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.last_name)


class Rol(models.Model):
    description = models.CharField(max_lenght=20)

    def __unicode__(self):
        return self.description


class Theatre(models.Model):
    name = models.CharFile(max_lenght=30, required=True)
    direction = models.CharFile(max_lenght=30, required=True)
    borough = models.CharFile(max_lenght=15)
    city = models.CharFile(max_lenght=15)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Genre(models.Model):
    name = models.CharFile(max_lenght=15)

    def __unicode__(self):
        return self.name


class Play(models.Model):
    title = models.CharFile(max_lenght=50, required=True)
    release_date = models.DateTimeField()
    genre = models.ForeignKey(Genre, required=True)
    current_theater = models.ForeignKey(Theatre, required=True)
    members = models.ManyToManyField(Member)
    pictures_book = models.ManyToManyField('Image')

    def __unicode__(self):
        return self.title


# for index page configuration
# class Cover(models.Model):
    # '''FIXME'''
    # num_images = models.IntField(required=True, max_value=3)
    # images = db.ListField(db.ReferenceField('Image'), required=True)


class Image(models.Model):
    name = models.CharFile(max_lenght=50, required=True)
    image = models.ImageField(required=True)

    def __unicode__(self):
        return self.name
