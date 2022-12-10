# Generated by Django 3.2 on 2022-12-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Borrador', 'Borrador'), ('Publicado', 'Publicado'), ('Retirado', 'Retirado')], default='Borrador', max_length=10)),
                ('producto', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='nombre/%Y/%m/%d')),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha de Publicacion')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
