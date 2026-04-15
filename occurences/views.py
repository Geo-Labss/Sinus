from rest_framework import generics
from occurences.models import Occorrencia
from occurences.serializers import occurencesSerializer


class OcorrenciaCreateListView(generics.ListCreateAPIView):
    queryset = Occorrencia.objects.all()
    serializer_class = occurencesSerializer


class OcorrenciaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Occorrencia.objects.all()
    serializer_class = occurencesSerializer