from django.urls import path
from . import views


urlpatterns = [
    path('', views.CuisineListView.as_view(), name='cuisine_list_cls'),

    path('<slug:slug>/', 
         views.CuisineDetailView.as_view(), 
         name='Cuisine_detail'),
]