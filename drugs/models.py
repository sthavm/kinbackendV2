from django.db import models
import uuid

# Create your models here.

SPECIFIC_DAYS = 'specific_days'
AS_NEEDED = 'as_needed'
ODD_EVEN_DAYS = 'odd_even_days'
ODD_DAYS = 'odd_days'
EVEN_DAYS = 'even_days'
DATE_DURATIONS = 'date_durations'
EVERYDAY = 'everyday'
EVERY_N_DAY = 'every-n-day'
FREQUENCY_TYPE_CHOICES = [
        (SPECIFIC_DAYS, 'SPECIFIC_DAYS'),
		(AS_NEEDED, 'AS_NEEDED'),
		(ODD_EVEN_DAYS, 'ODD_EVEN_DAYS'),
		(ODD_DAYS, 'ODD_DAYS'),
		(EVEN_DAYS, 'EVEN_DAYS'),
		(DATE_DURATIONS, 'DATE_DURATIONS'),
		(EVERYDAY, 'EVERYDAY'),
		(EVERY_N_DAY, 'EVERY-N-DAY'),
    ]
MONDAY = 'Monday'
TUESDAY = 'Tuesday'
WEDNESDAY = 'Wednesday'
THURSDAY = 'Thursday'
FRIDAY = 'Friday'
SATURDAY = 'Saturday'
SUNDAY = 'Sunday'
DAY_CHOICES = [
		(MONDAY, 'Monday'),
		(TUESDAY, 'Tuesday'),
		(WEDNESDAY, 'Wednesday'),
		(THURSDAY, 'Thursday'),
		(FRIDAY, 'Friday'),
		(SATURDAY, 'Saturday'),
		(SUNDAY, 'Sunday')
]

class DemoDrug(models.Model):
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	drugName = models.CharField(max_length=64)
	quantityInKindo = models.PositiveSmallIntegerField(null=True, blank=True)
	strength = models.PositiveSmallIntegerField()
	unit = models.CharField(max_length=10, default='mg')
	frequencyType = models.CharField(
        max_length=20,
        choices=FREQUENCY_TYPE_CHOICES,
        default=EVERYDAY,
    )
	everyN = models.PositiveSmallIntegerField(blank=True, null=True)
	expiryDate = models.DateField(null=True, blank=True)
	storedInKindo = models.BooleanField(blank=True, null=True)
	isDispensable = models.BooleanField(default=True)
	canisterNFC = models.CharField(max_length=64, null=True, blank=True)
	canisterString = models.CharField(max_length=64, null=True, blank=True)
	specialInstructions = models.CharField(max_length=1024, null=True, blank=True)
	startDate = models.DateField(null=True, blank=True)
	endDate = models.DateField(null=True, blank=True)
	isStorable = models.BooleanField(default=True)
	typeOfDrug = models.CharField(max_length=64, null=True, blank=True)
	origin = models.CharField(max_length=64, null=True, blank=True)
	suspended = models.BooleanField(default=False)
	suspendDate = models.DateField(null=True, blank=True)

class Quantity(models.Model):
    drug = models.ForeignKey(DemoDrug, on_delete=models.CASCADE, related_name='quantities')
    number = models.PositiveSmallIntegerField(blank=True, null=True)

class Time(models.Model):
    drug = models.ForeignKey(DemoDrug, on_delete=models.CASCADE, related_name='times')
    time = models.TimeField(blank=True, null=True)

class Day(models.Model):
    drug = models.ForeignKey(DemoDrug, on_delete=models.CASCADE, related_name='days')
    day = models.CharField(choices=DAY_CHOICES, blank=True, max_length=10, null=True)