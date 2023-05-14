from .views import *
from django.urls import path
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('room_detail/<slug>', RoomDetailView.as_view(), name='room_detail'),
    path('room-list', RoomListView.as_view(), name='room_list'),
    path('search', room_search, name='search'),
    path('add-room', AddRoom.as_view(), name='add_room'),
    path('contacts', contact, name='contact'),
    path('about', about, name='about'),
    path('room_review/<slug>', room_review, name='room_review'),

    # path('room_review/<slug>', room_review, name='room_review'),
]