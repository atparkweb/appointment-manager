import graphene
from graphene_django import DjangoObjectType
from .models import Appointment, Attendee


class AppointmentType(DjangoObjectType):
    class Meta:
        model = Appointment
        fields = '__all__'

class AttendeeType(DjangoObjectType):
    class Meta:
        model = Attendee
        fields = ('id', 'first_name', 'last_name')

class Query(graphene.ObjectType):
    all_appointments = graphene.List(AppointmentType)
    all_attendees = graphene.List(AttendeeType)

    def resolve_all_appointments(root, info):
        return Appointment.objects.all()

    def resolve_all_attendees(root, info):
        return Attendee.objects.all()

schema = graphene.Schema(query=Query)
