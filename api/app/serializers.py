from rest_framework import serializers
from .models import *
class Sample(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    email=serializers.EmailField()
    place=serializers.CharField()

class Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Project_user
        fields='__all__'