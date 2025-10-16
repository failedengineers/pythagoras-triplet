from rest_framework import serializers
from .models import triplets
class tripletsserializer(serializers.ModelSerializer):
    class Meta:
        model=triplets
        fields="__all__"

