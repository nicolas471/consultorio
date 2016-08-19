from flask_admin.contrib.mongoengine import ModelView
from consultorioWeb.models import Member, Play, Cover, Genre, Theatre, Image


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
