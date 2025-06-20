from account.serializers import UserSerializer
from .models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    #user = UserSerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = ('id', 'company', 'position', 'status', 'date_applied',)

class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('company', 'position', 'status', 'date_applied')
