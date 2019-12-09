# Generated by Django 2.2.6 on 2019-10-03 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0004_remove_photos_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photos',
            options={'ordering': ['-created', '-quant_like'], 'verbose_name': 'Foto', 'verbose_name_plural': 'Fotos'},
        ),
        migrations.AddField(
            model_name='photos',
            name='quant_like',
            field=models.IntegerField(blank=True, default=0, verbose_name='Curtidas'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to='photos/media', verbose_name='Foto'),
        ),
        migrations.RemoveField(
            model_name='photos',
            name='like',
        ),
        migrations.AddField(
            model_name='photos',
            name='like',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
