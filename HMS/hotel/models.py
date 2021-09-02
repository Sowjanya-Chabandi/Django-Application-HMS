from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Room(models.Model):
    Room_Categories={
        ('AC','AC'),('NonAC','NonAC'),('Deluxe','Deluxe'),('Suite','Suite')}
    roomnum=models.IntegerField()
    roomtype=models.CharField(max_length=6,choices=Room_Categories)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    
    def __str__(self):
        return f'RoomNum-{self.roomnum},{self.roomtype}'
    def get_absolute_url(self):
        return reverse('room-detail',kwargs={'pk':self.pk})

class Table(models.Model):
    tablenum=models.IntegerField()
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    #user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'TableNum-{self.tablenum}'
    def get_absolute_url(self):
        return reverse('table-detail',kwargs={'pk':self.pk})

class Menu(models.Model):
    menu_categories={('Breakfast','Breakfast'),('Lunch','Lunch'),('Dinner','Dinner')}
    #menu_categories={'Breakfast':['Dosa','Idli','Puri'],'Lunch':['VegBriyani','ChickenBriyani'],'Dinner':['VegBiryani','ChickenBriyani','Roti','Dosa']}
    menu=models.CharField(max_length=10,choices=menu_categories)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.menu} '

    
