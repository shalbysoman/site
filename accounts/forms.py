from django.forms import ModelForm
from .models import Registration


class RegistrationForm(ModelForm):
    class Meta:
        # the Model from which the form will inherit from
        model = Registration
        # the fields we want from the Model
        fields = '__all__'
        # styling the form with bootstrap classes

