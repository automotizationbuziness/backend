from django.forms import ModelForm
from .models import Tour
import django.forms as forms


class TourForm(ModelForm):
    class Meta:

        
        model = Tour
        fields = '__all__'
        widgets = {'cost': forms.TextInput(attrs={'data-mask': '00000.0000'})}
