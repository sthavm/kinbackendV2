from django.db import models
import uuid

# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    EVENT_TYPES = [
        ('dispensed_on_time','Dispensed on time' ),
        ('dispensed_on_time_incomplete','Dispensed on time (incomplete)'),
        ('late_dispense','Late Dispense' ),
        ('late_dispense_incomplete','Late Dispense (incomplete)' ),
        ('missed','Missed'),
        ('dispensed_to_cup_session','Dispensed to cup (by session)'),
        ('dispensed_to_cup_drug','Dispensed to cup (by drug)'),
        ('dispensed_to_pillbox','Dispensed to pillbox'),
        ('incomplete_dispense','Incomplete Dispense')
    ]
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    date_time = models.DateTimeField()


class DispensedSession(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='dispensed_session')

class DispensedDrug(models.Model):
    CHOICES = [('dispensed','Dispensed'),('manual','Manual'),('skipped','Skipped')]
    drug_text = models.CharField(max_length=80)
    quantity_to_be_taken = models.PositiveSmallIntegerField(blank=True, null=True)
    quantity_actually_taken = models.PositiveSmallIntegerField(blank=True, null=True)
    dispense_status = models.CharField(choices=CHOICES, max_length=40)
    dispensed_session = models.ForeignKey(DispensedSession, on_delete=models.CASCADE, related_name='dispensed_drug')
    def __str__(self) -> str:
        return self.drug_text
