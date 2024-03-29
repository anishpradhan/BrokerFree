# Generated by Django 3.2.18 on 2023-05-13 18:55

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='furnishing',
            field=models.CharField(choices=[('Full-Furnished', 'Full-Furnished'), ('Semi-Furnished', 'Semi-Furnished '), ('Non-Furnished', 'Non-Furnished')], max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image_1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image_2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image_3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='media'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image_4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='media'),
        ),
    ]
