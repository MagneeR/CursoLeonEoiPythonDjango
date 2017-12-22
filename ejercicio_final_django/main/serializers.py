from rest_framework import serializers
from .models import *

class CombatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combat
        fields = ('url', 'id', 'date', 'fighter1', 'fighter2', 'tournament')
"""'__all__'  Mete todo esto de golpe ('url', 'date', 'fighter1', 'fighter2', 'tournament')"""

class FighterSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Fighter
       fields = ('url', 'alias', 'avatar', 'force', 'skill', 'resistance')

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    #fighters = serializers.StringRelatedField(many=True)
    #combats = serializers.StringRelatedField(many=True)
    combats = CombatSerializer(many=True, read_only=True)
    fighters = FighterSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = ('url', 'name', 'start_date', 'finish_date', 'fighter_count', 'category', 'fighters', 'combats')

