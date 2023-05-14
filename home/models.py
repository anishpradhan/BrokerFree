from django.db import models
from django_resized import ResizedImageField
from django.utils.text import slugify
from django.conf import settings
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator




class Room(models.Model):
    furnishing_choice = (
        ('Full-Furnished', 'Full-Furnished'),
        ('Semi-Furnished', 'Semi-Furnished '),
        ('Non-Furnished', 'Non-Furnished'))
    type_choices = (
        ('Flat', 'Flat'),
        ('Single Room', 'Single Room'),
        ('Apartment', 'Apartment'),
    )
    author_type_choices = (
        ('Owner', 'Owner'),
        ('Agent', 'Agent'),
    )
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/', blank=True)
    image_1 = ResizedImageField(upload_to='media/', blank=True)
    image_2 = ResizedImageField(upload_to='media/', blank=True)
    image_3 = ResizedImageField(upload_to='media/', blank=True)
    image_4 = ResizedImageField(upload_to='media/', blank=True)
    description = RichTextField()
    furnishing = models.CharField(max_length=50, choices=furnishing_choice)
    num_bedroom = models.IntegerField()
    num_bathroom = models.IntegerField()
    num_livingroom = models.IntegerField()
    num_kitchen = models.IntegerField()
    author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_agent_or_owner = models.CharField(max_length=500, choices=author_type_choices, default='Owner')
    contact_num = models.CharField(max_length=10)
    published_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=500, choices=type_choices )
    slug = models.SlugField(max_length=500,unique=True, blank=True)
    location = models.CharField(max_length=500)
    district = models.CharField(max_length=500)
    google_maps_embed_url = models.URLField(max_length=500,blank = True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Room, self).save(*args, **kwargs)


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review = models.TextField()
    review_published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.author.username+' on '+self.room.title


