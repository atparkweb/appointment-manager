from django.db import models
from django_enumfield import enum

class Status(enum.Enum):
    PENDING = 0
    COMPLETE = 1
    CANCELLED = 2

class Appointment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = enum.EnumField(Status, default=Status.PENDING)
    owner = models.ForeignKey('Attendee', related_name='appointments_owner', on_delete=models.CASCADE)
    attendees = models.ManyToManyField('Attendee', related_name='appointments')

    class Meta:
        ordering = ['date', 'start_time']

    def __str__(self):
        return self.title

class Attendee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name
