# Generated by Django 3.0.3 on 2020-03-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=5)),
                ('ciudad', models.CharField(max_length=60)),
                ('estado', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Editores',
                'ordering': ['nombre'],
            },
        ),
    ]
