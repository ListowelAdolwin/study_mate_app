from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
]
