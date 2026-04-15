from rest_framework import serializers
from occurences.models import Occorrencia


class occurencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occorrencia
        fields = '__all__'