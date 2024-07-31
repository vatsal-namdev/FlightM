# Flights Management System

It is a Django-based application that provides real-time flight status updates and notifications to passengers. Users can subscribe to flight updates and receive email notifications for any changes in flight status.

## Features

- Real-time flight status updates
- User subscription for flight status notifications
- Email notifications for flight status changes
- Admin panel for managing flights and statuses

## Technologies Used

- Django
- Celery
- RabbitMQ
- PostgreSQL
- Docker

## Prerequisites

- Python 3.10
- Docker
- Docker Compose
- Git

## Setup

### Clone the Repository

git clone https://github.com/vatsal-namdev/FlightM.git
cd FlightM

## Environment Variables

- SECRET_KEY=your_secret_key
- DEBUG=True
- ALLOWED_HOSTS=localhost,127.0.0.1
- DATABASE_URL=postgres://user:password@db:5432/ams
- EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
- EMAIL_HOST=smtp.gmail.com
- EMAIL_PORT=587
- EMAIL_USE_TLS=True
- EMAIL_HOST_USER=your_email@gmail.com
- EMAIL_HOST_PASSWORD=your_email_password
- CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672/


## Docker Setup

docker-compose up --build

## Apply Migrations

docker-compose exec web python manage.py migrate

## Create a Superuser

docker-compose exec web python manage.py createsuperuser


## Access the Application
The application will be available at http://localhost:8000

## Updating Flight Statuses
Manually update in mock_data.json, after that trigger the update

docker-compose exec web python manage.py shell
- from flight.tasks import update_flight_status_task
- update_flight_status_task.delay()

### Thankyou!!

