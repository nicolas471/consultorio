from django.db import models


class Carrousel(models.Model):

    class Meta():
        verbose_name_plural = 'Carrousel'

    image = models.ImageField(upload_to='carrousel')
