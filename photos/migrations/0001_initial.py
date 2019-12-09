# Generated by Django 2.2.6 on 2019-10-03 01:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Foto')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('like', models.IntegerField(blank=True, default=0, verbose_name='Curtidas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Enviada em')),
                ('aproved', models.BooleanField(blank=True, default=False, verbose_name='Aprovada?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to=settings.AUTH_USER_MODEL, verbose_name='Enviado por')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'ordering': ['-created', '-like'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Curtido por')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='photos.Photos', verbose_name='foto')),
            ],
            options={
                'verbose_name': 'Curtida',
                'verbose_name_plural': 'Curtidas',
            },
        ),
    ]
