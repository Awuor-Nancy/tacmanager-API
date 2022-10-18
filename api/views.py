from django.shortcuts import render
from .serializers import BillSerializer, TaxSerializer, TeamSerializer
from .models import Bills, Tax, Team
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from rest_framework.response import Response
# from rest_framework import generics, permissions
from rest_framework import viewsets


# Create your views here.
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()

    serializer_class = BillSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()

    serializer_class = TaxSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()

    serializer_class = TeamSerializer



