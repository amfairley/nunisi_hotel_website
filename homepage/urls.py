from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('nunisi_water/', views.water, name="water"),
    path('rooms/', views.rooms, name="rooms"),
    path('gallery/', views.gallery, name="gallery"),
]
