from rest_framework import serializers
from zdarzenia.models import Zdarzenie
class ZdarzenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zdarzenie
        fields = ['id', 'data_dodania', 'data_zdarzenia', 'typ_zdarzenia', 'zasob', 'opis']
