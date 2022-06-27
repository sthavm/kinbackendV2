from django.urls import path

from . import views

urlpatterns = [
    path('', views.DrugListCreate.as_view(), name='druglist'),
    path('delete/', views.DrugDeleteView.as_view(), name='delete_all')
]