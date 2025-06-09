from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Job
from .forms import JobForm
from .serializers import CreateJobSerializer

@api_view(['POST'])
def create_job(request):
    form = JobForm(request.data)
    if form.is_valid():
        job = form.save(commit=False)
        job.user = request.user
        job.save()
        serializer = CreateJobSerializer(job)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'error add later'})
    
@api_view(['GET'])
def get_jobs(request):  
    user = request.user  
    jobs = Job.objects.filter(user = user)

    serializer = CreateJobSerializer(jobs, many=True)   
    print(jobs) 

    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
def delete_job(request, id):
    pass