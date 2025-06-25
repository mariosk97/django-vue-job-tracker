from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Job
from .forms import JobForm
from .serializers import CreateJobSerializer, JobSerializer

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

    serializer = JobSerializer(jobs, many=True)   
    print(jobs) 

    return JsonResponse(serializer.data, safe=False)

@api_view(['DELETE'])
def delete_job(request, id):
    job = Job.objects.get(id = id, user = request.user)
    job.delete()

    return JsonResponse({'message': 'Job deleted'})

@api_view(['PUT'])
def update_job(request, id):
    job = Job.objects.get(id = id, user = request.user)

    job.company = request.data.get('company')
    job.position = request.data.get('position')
    job.status = request.data.get('status')
    job.date_applied = request.data.get('date_applied')
    job.save()

    return JsonResponse({'message': 'Job updated'})