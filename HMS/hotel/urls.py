from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import RoomListView,TableListView,MenuListView,RoomDetailView,TableDetailView,MenuDetailView,RoomCreateView,TableCreateView,RoomUpdateView,RoomDeleteView


urlpatterns=[
    path('',views.index,name='index'),
    #path('rooms',views.rooms,name='rooms'),
    path('rooms',RoomListView.as_view(),name='rooms'),
    #path('tables',views.tables,name='tables'),
    path('tables',TableListView.as_view(),name='tables'),
    #path('menu',views.menu,name='menu'),
    path('menu',MenuListView.as_view(),name='menu'),
    path('registration/',user_views.registration,name='registration'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('room/<int:pk>/',RoomDetailView.as_view(),name='room-detail'),
    path('table/<int:pk>/',TableDetailView.as_view(),name='table-detail'),
    path('menu/<int:pk>/',MenuDetailView.as_view(),name='menu-detail'),
    path('room/new/',RoomCreateView.as_view(),name='room-create'),
    path('table/new/',TableCreateView.as_view(),name='table-create'),
    path('room/<int:pk>/update',RoomUpdateView.as_view(),name='room-update'),
    
    path('room/<int:pk>/delete',RoomDeleteView.as_view(),name='room-delete'),
    path('about/',views.about,name='about'),
    path('bookings/',views.bookings,name='bookings'),
    ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
