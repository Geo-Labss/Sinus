from rest_framework import generics
from Secretaria.models import Secretaria
from Secretaria.serializers import SecretariaSerializer

class SecretariaListCreate(generics.ListCreateAPIView):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer

class SecretariaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Secretaria.objects.all()
    serializer_class = SecretariaSerializer