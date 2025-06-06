from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_job(request):
    print(request.data.get('company'))
    message = 'done!'

    return JsonResponse({'message': message})