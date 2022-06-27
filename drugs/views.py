from django.http import HttpResponse
from django.shortcuts import render
from drugs.models import DemoDrug, Quantity, Day, Time
from rest_framework.generics import ListCreateAPIView
from drugs.serializers import DemoDrugSerializer, DaySerializer, TimeSerializer, QuantitySerializer
from django.views import View

# Create your views here.

class DrugListCreate(ListCreateAPIView):
    queryset = DemoDrug.objects.all()
    serializer_class = DemoDrugSerializer

class DrugDeleteView(View):
    def get(self,request):
        DemoDrug.objects.all().delete()
        return HttpResponse('deleted')