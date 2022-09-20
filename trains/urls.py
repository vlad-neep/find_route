from django.contrib import admin
from django.urls import path
from cities.views import *
from trains.views import *


urlpatterns = [
    # path('', home, name='home'),
    path('', TrainListView.as_view(), name='home'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
]