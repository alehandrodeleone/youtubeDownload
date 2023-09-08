from .models import *
from rest_framework import serializers

class list_serializer(serializers.ModelSerializer):
    class Meta:
        model=links
        fields=["id","Links","datetime"]