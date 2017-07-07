from django.db import models


class Carrousel(models.Model):
    image = models.ImageField(upload_to='carrousel')
