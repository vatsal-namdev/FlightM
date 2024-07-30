# forms.py

from django import forms
from .models import Subscriber, Flight

class SubscriptionForm(forms.ModelForm):
    flight = forms.ModelChoiceField(queryset=Flight.objects.all(), required=True)

    class Meta:
        model = Subscriber
        fields = ['flight', 'email']
