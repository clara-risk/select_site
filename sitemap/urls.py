from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('map/', views.map, name='map'),
    path('map2/', views.map2, name='map2'),
    path('map3/', views.map3, name='map3'),
    path('map4/', views.map4, name='map4'),
    path('map5/', views.map5, name='map5'),
    path('map6/', views.map6, name='map6'),
]
