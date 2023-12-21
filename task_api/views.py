from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Task
from .serializer import TaskSerializer


@api_view(['GET', 'POST'])
def task_list(request):

    #Lists all tasks
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    #Creates new task
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])


def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=404)

    #get single task
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    #update a task
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    #delete task
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)
