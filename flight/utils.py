import json
from django.utils import timezone
from .models import Flight, FlightStatus, Notification
from .fcm_utils import send_notification

def fetch_flight_data():
    """
    Fetch flight data from a mock data source.
    """
    with open('mock_data.json') as f:
        data = json.load(f)
        print("....................loaded")
    return data

def update_flight_status():
    """
    Update flight status based on fetched flight data.
    """
    data = fetch_flight_data()
    for item in data:
        flight, created = Flight.objects.get_or_create(
            flight_number=item['flight_number'],
            defaults={
                'departure': item['departure'],
                'destination': item['destination'],
                'scheduled_time': item['scheduled_time']
            }
        )
        FlightStatus.objects.create(
            flight=flight,
            status=item['status'],
            updated_time=timezone.now()
        )

def notify_passengers(flight_id, message):
    """
    Notify passengers about flight status changes.
    """
    flight = Flight.objects.get(id=flight_id)
    notification = Notification.objects.create(flight=flight, message=message)
    # Assume passengers have a device token stored in the database
    # For now, we'll use a mock token
    token = "mock_device_token"
    send_notification(token, message)
