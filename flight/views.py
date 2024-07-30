from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flight, FlightStatus, Subscriber
from .tasks import update_flight_status_task
from .forms import SubscriptionForm

def trigger_update(request):
    update_flight_status_task.delay()
    print("Trigger Update Task Called")
    return HttpResponse("Flight data update triggered.")

def flight_list(request):
    flights = Flight.objects.all()
    flight_statuses = FlightStatus.objects.all()
    context = {
        'flights': flights,
        'flight_statuses': flight_statuses
    }
    return render(request, 'flight.html', context)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_success')
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})

def subscription_success(request):
    return render(request, 'subscription_success.html')
