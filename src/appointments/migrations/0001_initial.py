# Generated by Django 4.2.2 on 2023-06-21 02:33

import appointments.models
from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', django_enumfield.db.fields.EnumField(default='pending', enum=appointments.models.Status)),
                ('attendees', models.ManyToManyField(related_name='appointments', to='appointments.attendee')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_owner', to='appointments.attendee')),
            ],
            options={
                'ordering': ['date', 'start_time'],
            },
        ),
    ]