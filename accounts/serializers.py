from .models import *
from rest_framework import serializers


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

