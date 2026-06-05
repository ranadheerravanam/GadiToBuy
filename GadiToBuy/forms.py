from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle

        fields = [
            'title',
            'brand',
            'model',
            'year',
            'price',
            'kilometers',
            'fuel_type',
            'location',
            'description',
            'image'
        ]