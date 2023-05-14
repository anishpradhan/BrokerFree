# Generated by Django 3.2.18 on 2023-05-12 19:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_room_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='property_details',
        ),
        migrations.AddField(
            model_name='room',
            name='contact_num',
            field=models.CharField(default=9817325641, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='furnishing',
            field=models.CharField(choices=[('Full-Furnished', 'Full-Furnished'), ('Semi-Furnished', 'Semi-Furnished '), ('Not-Furnished', 'Not-Furnished')], default='Full-Furnished', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='num_bathroom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='num_bedroom',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='num_kitchen',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='num_livingroom',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]