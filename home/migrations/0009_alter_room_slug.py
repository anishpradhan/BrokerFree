# Generated by Django 3.2.18 on 2023-05-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20230513_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]
