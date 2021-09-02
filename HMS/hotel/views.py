from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Room,Table,Menu
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

def index(request):
    return render(request,'hotel/index.html')

myDate = datetime.now()
'''text=[
    {'roomtype':'AC','roomnum':'1'},
    {'roomtype':'NAC','roomnum':'2'}
    ]

text1=[
    {'tablenum':'1'},
    {'tablenum':'2'}
    ]

text2=[
    {'menutype':'breakfast','menu':'Dosa'},
    {'menutype':'Lunch','menu':'Meal'}
    ]
'''

def rooms(request):
    context={'text':Room.objects.all()}
    return render(request,'hotel/rooms.html',context)

def tables(request):
    context1={'text1':Table.objects.all()}
    return render(request,'hotel/tables.html',context1)

def menu(request):
    context2={'text2':Menu.objects.all()}
    #menu_categories={'Breakfast':['Dosa','Idli','Puri'],'Lunch':['VegBriyani','ChickenBriyani'],'Dinner':['VegBiryani','ChickenBriyani','Roti','Dosa']}
    #return render(request,'hotel/menu.html',menu_categories)
    return render(request,'hotel/menu.html',context2)

class RoomListView(ListView):
    model=Room
    template_name='hotel/rooms.html'
    context_object_name='text'
    ordering=['roomnum']

class TableListView(ListView):
    model=Table
    template_name='hotel/tables.html'
    context_object_name='text1'
    ordering=['tablenum']

class MenuListView(ListView):
    model=Menu
    template_name='hotel/menu.html'
    context_object_name='text2'
    ordering=['menu']

class RoomDetailView(DetailView):
    model=Room

class TableDetailView(DetailView):
    model=Table

class MenuDetailView(DetailView):
    model=Menu

class RoomCreateView(CreateView):
    model=Room
    fields=['roomtype','roomnum','check_in','check_out']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
class TableCreateView(CreateView):
    model=Table
    fields=['tablenum','check_in','check_out']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class RoomUpdateView(UserPassesTestMixin,UpdateView):
    model=Room
    fields=['roomtype','roomnum','check_in','check_out']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        room=self.get_object()
        if self.request.user==room.user:
            return True
        return False

class RoomDeleteView(UserPassesTestMixin,DeleteView):
    model=Room
    success_url='/'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        room=self.get_object()
        if self.request.user==room.user:
            return True
        return False

def about(request):
    return render(request,'hotel/about.html')

def bookings(request):
    #userdetails={'roomtype':user.roomtype,'roomnum':user.roomnum,'check_in':user.check_in,'check_out':user.check_out}
    
    return render(request,'hotel/bookings.html')



