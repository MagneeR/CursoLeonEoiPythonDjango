from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.
class FighterViewSet(viewsets.ModelViewSet):
   queryset = Fighter.objects.all()
   serializer_class = FighterSerializer

class TournamentsViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class CombatViewSet(viewsets.ModelViewSet):
    queryset = Combat.objects.all()
    serializer_class = CombatSerializer

