from django.shortcuts import render
from .serializers import BillSerializer, TaxSerializer, TeamSerializer
from .models import Bills, Tax, Team
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, permissions


# Create your views here.

