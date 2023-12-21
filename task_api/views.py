from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all_task(request):
    pass

@api_view(['GET'])
def get_task(request, id):
    pass

@api_view(['POST'])
def create_task(request):
    pass

@api_view(['PUT'])
def update_task(request, id):
    pass

@api_view(['DELETE'])
def delete_task(request, id):
    pass