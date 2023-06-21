from django.contrib import admin

from .models import Appointment, Attendee

admin.site.register(Appointment)
admin.site.register(Attendee)
admin.site.site_header = 'Appointment Manager'
