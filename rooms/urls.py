from django.urls import path

from .views import room,room_detail
urlpatterns =[
    path("rooms/",room,name="rooms"),
    path("<slug:slug>/",room_detail,name="room"),
   
   


]