from rest_framework import generics
from rest_framework.decorators import api_view



from .serializers import RecordListSerializer, RecordDetailSerializer
from .models import Record

class RecordListApi(generics.ListCreateAPIView):
    serializer_class = RecordListSerializer
    queryset = Record.objects.all()



class RecordDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecordDetailSerializer
    queryset = Record.objects.all()