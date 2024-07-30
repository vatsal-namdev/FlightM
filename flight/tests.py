from django.test import TestCase
from unittest.mock import patch
from django.utils import timezone
from .models import Flight, FlightStatus, Notification
from .utils import fetch_flight_data, update_flight_status, notify_passengers

class FlightTests(TestCase):

    def setUp(self):
        # Setup mock data if necessary
        pass

    def test_fetch_flight_data(self):
        data = fetch_flight_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_update_flight_status(self):
        update_flight_status()
        # Check if Flight and FlightStatus records are created
        self.assertTrue(Flight.objects.exists())
        self.assertTrue(FlightStatus.objects.exists())

    @patch('flight.utils.send_notification')  # Mock send_notification in utils
    def test_notify_passengers(self, mock_send_notification):
        flight = Flight.objects.create(
            flight_number="ABC123",
            departure="City A",
            destination="City B",
            scheduled_time=timezone.now()
        )
        notify_passengers(flight.id, "Test notification message")
        
        # Check if Notification record is created
        self.assertTrue(Notification.objects.exists())
        
        # Verify that send_notification was called with the correct arguments
        mock_send_notification.assert_called_once_with("mock_device_token", "Test notification message")
