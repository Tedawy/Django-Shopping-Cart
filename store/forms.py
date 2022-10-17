from django import forms
from .models import UserOrder
from django.core.exceptions import ValidationError


class OrdersForm(forms.ModelForm):

    class Meta:
        model = UserOrder
        fields = '__all__'
