from django.urls import path
from .views import flight_list, trigger_update, subscribe, subscription_success

urlpatterns = [
    path('', flight_list, name='flight_list'),
    path('trigger-update/', trigger_update, name='trigger_update'),
    path('subscribe/', subscribe, name='subscribe'),
    path('subscription-success/', subscription_success, name='subscription_success'),
]
