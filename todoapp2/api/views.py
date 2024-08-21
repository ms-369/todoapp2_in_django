from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Task


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:key>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:key>/',
		'Delete':'/task-delete/<str:key>/',
		}

	return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, key):
    task = Task.objects.get(id=key)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, key):
    task = Task.objects.get(id=key)
    task.delete()
    return Response('ITEM DELETED!!!')

@api_view(['POST'])
def taskUpdate(request, key):
    task = Task.objects.get(id=key)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
