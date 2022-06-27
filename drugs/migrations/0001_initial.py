# Generated by Django 4.0.5 on 2022-06-27 06:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoDrug',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('drugName', models.CharField(max_length=64)),
                ('quantityInKindo', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('strength', models.PositiveSmallIntegerField()),
                ('unit', models.CharField(default='mg', max_length=10)),
                ('frequencyType', models.CharField(choices=[('specific_days', 'SPECIFIC_DAYS'), ('as_needed', 'AS_NEEDED'), ('odd_even_days', 'ODD_EVEN_DAYS'), ('odd_days', 'ODD_DAYS'), ('even_days', 'EVEN_DAYS'), ('date_durations', 'DATE_DURATIONS'), ('everyday', 'EVERYDAY'), ('every-n-day', 'EVERY-N-DAY')], default='everyday', max_length=20)),
                ('everyN', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('expiryDate', models.DateField(blank=True, null=True)),
                ('storedInKindo', models.BooleanField(blank=True)),
                ('isDispensable', models.BooleanField(default=True)),
                ('canisterNFC', models.CharField(blank=True, max_length=64, null=True)),
                ('canisterString', models.CharField(blank=True, max_length=64, null=True)),
                ('specialInstructions', models.CharField(blank=True, max_length=1024, null=True)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('isStorable', models.BooleanField(default=True)),
                ('typeOfDrug', models.CharField(blank=True, max_length=64, null=True)),
                ('origin', models.CharField(blank=True, max_length=64, null=True)),
                ('suspended', models.BooleanField(default=False)),
                ('suspendDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='drugs.demodrug')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantities', to='drugs.demodrug')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, null=True)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='drugs.demodrug')),
            ],
        ),
    ]