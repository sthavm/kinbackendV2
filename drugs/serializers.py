from rest_framework import serializers
from drugs.models import DemoDrug, Time, Day, Quantity
from datetime import datetime

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['day']

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['time']

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        fields = ['number'] 

class DemoDrugSerializer(serializers.ModelSerializer):
    # days = serializers.PrimaryKeyRelatedField(many=True, queryset=Day.objects.all())
    # times = serializers.PrimaryKeyRelatedField(many=True, queryset=Time.objects.all())
    # quantities = serializers.PrimaryKeyRelatedField(many=True, queryset=Quantity.objects.all())
    days = DaySerializer(many=True)
    times = TimeSerializer(many=True)
    quantities = QuantitySerializer(many=True)

    class Meta:
        model = DemoDrug
        fields = ['id','drugName','strength', 'unit','frequencyType','quantities','times','days', 'expiryDate', 'storedInKindo','isDispensable','canisterNFC','canisterString','specialInstructions','startDate','isStorable','typeOfDrug','origin']

    def create(self, validated_data):
        print(validated_data)
        day_data = validated_data.pop('days')
        time_data = validated_data.pop('times')
        quantity_data = validated_data.pop('quantities')
        drug = DemoDrug.objects.create(**validated_data)        
        for day in day_data:
            Day.objects.create(drug=drug, **day)
        for time in time_data:
            Time.objects.create(drug=drug, **time)
        for quantity in quantity_data:
            Quantity.objects.create(drug=drug, **quantity)
        return drug
