from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventListCreate.as_view(), name='eventlist'),
    path('delete/', views.EventDeleteView.as_view(), 'delete_all')
]