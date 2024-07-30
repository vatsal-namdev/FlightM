from django.contrib import admin
from .models import Flight, FlightStatus, Notification, Subscriber

# Register your models here.
admin.site.register(Flight)
admin.site.register(FlightStatus)
admin.site.register(Notification)
admin.site.register(Subscriber)
