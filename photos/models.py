from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Photos(models.Model):
    image = models.ImageField(
    		upload_to = 'photos/media',
    		verbose_name = 'Foto',
    		null=False,
    		blank=False
    	)
    title = models.CharField('Título', max_length=200)
    quant_like = models.IntegerField('Curtidas', blank=True, default=0)
    created = models.DateTimeField('Enviada em', auto_now_add=True)
    aproved = models.BooleanField('Aprovada?', blank=True, default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-created', '-quant_like']


class Like(models.Model):
    id_photo = models.IntegerField(
        'id_foto', blank=False
    )
    author = models.IntegerField(
        'id_user', blank=False
    )
    class Meta:
        verbose_name = 'Curtida'
        verbose_name_plural = 'Curtidas'
