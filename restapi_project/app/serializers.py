from rest_framework import serializers
from .models import *

class Sample(serializers.Serializer):
    roll_no=serializers.Intergerfield()
    name=serializers.Charfield()
    age=serializers.Integerfield()
    email=serializers.EmailField()


class Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields='__all__'