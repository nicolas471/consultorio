from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birthdate = models.DateField()
    email = models.EmailField()
    profile_picture = models.ForeignKey('Image')
    rol = models.ForeignKey('Rol')

    def __str__(self):
        return '{0} {1}'.format(self.name, self.last_name)


class Rol(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self):
        return self.description


class Theatre(models.Model):
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    borough = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.ForeignKey(Genre)
    current_theater = models.ForeignKey(Theatre)
    members = models.ManyToManyField(Member)
    pictures_book = models.ManyToManyField('Image')

    def __str__(self):
        return self.title


# for index page configuration
# class Cover(models.Model):
    # '''FIXME'''
    # num_images = models.IntField(required=True, max_value=3)
    # images = db.ListField(db.ReferenceField('Image'))


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
