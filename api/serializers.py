from dataclasses import field
from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Bills, Tax, Team

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ('title', 'amount')

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ('title', 'amount')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('first_name', 'last_name', 'title', 'email', 'password')

                



