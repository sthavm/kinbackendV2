# Generated by Django 4.0.5 on 2022-06-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demodrug',
            name='storedInKindo',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]