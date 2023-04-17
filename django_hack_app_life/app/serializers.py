from rest_framework import serializers
from .models import Userdata


class MyModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userdata
        fields = ('klient_field', 'nomer_zajavki', 'inn', 'status')
