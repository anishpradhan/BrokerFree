from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
# Create your views here.



class HomeView(View):
    def get(self,request):
        top_offers = Room.objects.all().order_by('-id')[:6]
        location_search = Room.objects.values_list('location', flat=True).distinct()
        district_search = Room.objects.values_list('district', flat=True).distinct()
        type_search = Room.objects.values_list('type', flat=True).distinct()
        context = {
            'location_search':location_search,
            'district_search':district_search,
            'type_search':type_search,
            'top_offers':top_offers
        }
        return render(request,'home_1.html', context=context)



class RoomListView(View):
    def get(self,request):
        rooms = Room.objects.all()
        paginator = Paginator(rooms, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        location_search = Room.objects.values_list('location', flat=True).distinct()
        district_search = Room.objects.values_list('district', flat=True).distinct()
        type_search = Room.objects.values_list('type', flat=True).distinct()
        context = {
            'rooms':page_obj,
            'room_count':rooms.count(),
            'district_search':district_search,
            'location_search':location_search,
            'type_search':type_search,
            'total_pages': range(page_obj.paginator.num_pages),
        }
        return render(request, 'room-list.html', context=context)
    
class RoomDetailView(View):
    def get(self,request,slug):
        room = Room.objects.get(slug = slug)
        review = Review.objects.filter(room=room)
        paginator = Paginator(review, 4)
        page_number = request.GET.get("review_page")
        page_obj = paginator.get_page(page_number)
        recently_viewed = Room.objects.all().order_by('-published_date')[:8]
        context = {
            'room':room,
            'reviews':page_obj,
            'total_reviews': review.count(),
            'average_rating': review.aggregate(Avg('rating'))['rating__avg'],
            'recently_viewed':recently_viewed,
            
        }
        return render(request, 'room-detail_1.html', context=context)

def room_search(request):
    search_fields = {}
    rooms = Room.objects.all()
    if request.method == 'GET':
        if 'location' in request.GET:
            location = request.GET['location']
            if location and location != '':
                search_fields['location'] = location
                rooms = rooms.filter(location__iexact=location)
        
        if 'district' in request.GET:
            district = request.GET['district']
            if district and district != '':
                search_fields['district'] = district
                rooms = rooms.filter(district__iexact=district)

        if 'type' in request.GET:
            type = request.GET['type']
            if type and type != '':
                search_fields['type'] = type
                rooms = rooms.filter(type__iexact=type)

        paginator = Paginator(rooms, 12)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        location_search = Room.objects.values_list('location', flat=True).distinct()
        district_search = Room.objects.values_list('district', flat=True).distinct()
        context = {
            'rooms':page_obj,
            'room_count':rooms.count(),
            'location_search':location_search,
            'district_search':district_search,
            'total_pages': range(page_obj.paginator.num_pages),
            'search_fields':search_fields,
        }
        return render(request, 'room-list.html', context=context)
    else:
        return redirect('/room-list')
    

class AddRoom(LoginRequiredMixin, View ):
    login_url = '/login/'
    def get(self,request):
        return render(request, 'add-property.html')
    
    def post(self,request):
        if request.method == 'POST':
            title = request.POST['title']
            price = request.POST['price']
            images = request.FILES.getlist('images')
            description = request.POST['description']
            furnishing = request.POST['furnishing']
            num_bedroom = request.POST['num_bedroom']
            num_bathroom = request.POST['num_bathroom']
            num_livingroom = request.POST['num_livingroom']
            num_kitchen = request.POST['num_kitchen']
            author_agent_or_owner = request.POST['role']
            contact_num = request.POST['contact_num']
            location = request.POST['location']
            district = request.POST['district']
            type = request.POST['type']
            author = request.user
            google_maps_embed_url = request.POST['google_maps_url']

            image_dict = {
                'image':None,
                'image_1':None,
                'image_2':None,
                'image_3':None,
                'image_4':None,
            }
            for count, image in enumerate(images):
                if count == 0:
                    image_dict['image']=image
                else:
                    image_dict['image_'+str(count)]=image
            
            data = Room.objects.create(
                title=title,
                price=price,
                image=image_dict['image'],
                image_1=image_dict['image_1'],
                image_2=image_dict['image_2'],
                image_3=image_dict['image_3'],
                image_4=image_dict['image_4'],
                description=description,
                furnishing=furnishing,
                num_bedroom=num_bedroom,
                num_bathroom=num_bathroom,
                num_livingroom=num_livingroom,
                num_kitchen=num_kitchen,
                author_agent_or_owner=author_agent_or_owner,
                contact_num=contact_num,
                location=location,
                district=district,
                type=type,
                author=author,
                google_maps_embed_url=google_maps_embed_url
            )
            data.save()
            messages.success(request, 'The room is added!')
            return redirect('/room-list')

@login_required(login_url = 'login')
def room_review(request, slug):
    if request.method == 'POST':
        author = request.user
        room = Room.objects.get(slug=slug)
        rating = request.POST['rating']
        review = request.POST['review']
        data = Review.objects.create(
            author=author,
            room=room,
            rating=rating,
            review=review,
        )
        data.save()
        messages.success(request, 'The review is submitted!')
    return redirect(f'/room_detail/{room.slug}')


def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')