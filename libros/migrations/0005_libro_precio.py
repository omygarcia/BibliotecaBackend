# Generated by Django 3.0.3 on 2020-03-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0004_auto_20200301_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
