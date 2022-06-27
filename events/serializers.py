from rest_framework import serializers
from .models import Event, DispensedDrug, DispensedSession


class EventSerializer(serializers.ModelSerializer):
    dispensed_session = serializers.PrimaryKeyRelatedField(many=True, queryset=DispensedSession.objects.all())
    

    class Meta:
        model = Event
        fields = ['id','event_type','date_time','dispensed_session']
    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        session_data = validated_data.pop('dispensed_sessions')
        for session in session_data:
            created_session = DispensedSession.objects.create(event=event)
            drug_data = session.pop('dispensed_drugs')
            for drug in drug_data:
                DispensedDrug.objects.create(dispensed_session=created_session, **drug)
        return event

class DispensedSessionSerializer(serializers.ModelSerializer):
    dispensed_drug = serializers.PrimaryKeyRelatedField(many=True, queryset=DispensedDrug.objects.all())

    class Meta:
        model = DispensedSession
        fields = ['dispensed_drug']

class DispensedDrugSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DispensedDrug
        fields = ['drug_text', 'quantity_to_be_taken','quantity_actually_taken','dispense_status']

