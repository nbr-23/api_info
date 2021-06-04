from rest_framework import serializers
from .models import Employe, Depart

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class DepartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depart
        fields = '__all__'