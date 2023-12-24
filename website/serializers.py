from rest_framework import serializers
from .models import Record

class RecordListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields='__all__'


class RecordDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields='__all__'



