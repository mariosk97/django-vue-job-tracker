from account.serializers import UserSerializer
from .models import Job
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Job
        fields = ('id', 'user', 'company', 'position', 'status', 'date_applied',)