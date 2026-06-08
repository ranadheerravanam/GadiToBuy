from django import forms
from .models import Vehicle
from .models import Inquiry
from .models import Review
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
            'image',
            'status'
        ]
class InquiryForm(forms.ModelForm):

    class Meta:

        model = Inquiry

        fields = ['message']
class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review

        fields = [
            'rating',
            'comment'
        ]