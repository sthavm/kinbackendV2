from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, DispensedDrug, DispensedSession
from rest_framework.generics import ListCreateAPIView
from .serializers import EventSerializer, DispensedDrugSerializer, DispensedSessionSerializer
from django.views import View

# Create your views here.

class EventListCreate(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDeleteView(View):
    def get(self,request):
        Event.objects.all().delete()
        return HttpResponse('deleted')
    

