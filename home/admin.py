from django.contrib import admin
from .models import *

# Register your models here.


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'type', 'author',
                    'location', 'district', 'published_date')
    list_display_links = ('id', 'title', 'author')

    search_fields = ('id', 'title', 'location', 'district', 'author')
    list_filter = ('location', 'district', 'author')


admin.site.register(Room, RoomAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'room', 'rating',
                    'review', 'review_published_date')
    list_display_links = ('id', 'author', 'room')

    search_fields = ('id', 'author', 'room', 'rating')
    list_filter = ('rating', 'room', 'author')


admin.site.register(Review, ReviewAdmin)
