# Generated by Django 2.2.6 on 2019-10-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20191003_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/media', verbose_name='Foto'),
        ),
    ]
