from celery import shared_task
from django.utils import timezone
from .models import Flight, FlightStatus, Subscriber
from .utils import fetch_flight_data
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def update_flight_status_task():
    print("Task started: Fetching flight data...")
    data = fetch_flight_data()
    print("Fetched data:", data)
    
    for item in data:
        try:
            # Retrieve or create the flight
            flight, created = Flight.objects.get_or_create(
                flight_number=item['flight_number'],
                defaults={
                    'departure': item['departure'],
                    'destination': item['destination'],
                    'scheduled_time': item['scheduled_time']
                }
            )
            print(f"Flight {'created' if created else 'retrieved'}: {flight}")

            # Check if a status already exists for this flight
            flight_status, status_created = FlightStatus.objects.update_or_create(
                flight=flight,
                defaults={
                    'status': item['status'],
                    'updated_time': timezone.now()
                }
            )
            print(f"Status for flight {flight.flight_number} {'created' if status_created else 'updated'} to {item['status']}")


             # Notify subscribers
            if flight_status.status != item['status']:
                subscriptions = Subscriber.objects.filter(flight=flight)
                for subscription in subscriptions:
                    send_mail(
                        f'Update on flight {flight.flight_number}',
                        f'The status of flight {flight.flight_number} has been updated to {item["status"]}.',
                        settings.EMAIL_HOST_USER,
                        [subscription.email],
                        fail_silently=False,
                    )
                    print(f"Notification sent to {subscription.email}")

        except Exception as e:
            print(f"Error processing flight {item['flight_number']}: {e}")

    print("Flight status update task completed")
