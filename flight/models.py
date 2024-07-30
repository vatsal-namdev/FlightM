from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return self.flight_number

class FlightStatus(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.flight.flight_number} - {self.status}"

class Notification(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    message = models.TextField()
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.flight.flight_number} at {self.sent_time}"

class Subscriber(models.Model):
    email = models.EmailField()
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} subscribed to {self.flight.flight_number}"