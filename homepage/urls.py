from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('nunisi_water/', views.water, name="water")
]
