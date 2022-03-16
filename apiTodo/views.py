from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )
#*use decorators for rest_api
@api_view(['GET'])
def todoList(request):
    query = Todo.objects.all();
    #*using serializer
    serializer = TodoSerializer(query,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    
    #*using serializer
    serializer = TodoSerializer(data =request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

#*get and post together
@api_view(['GET','POST'])
def todoListCreate(request):
    query = Todo.objects.all();
    
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
    elif request.method == 'GET':
        serializer = TodoSerializer(query,many=True)
        
    return Response(serializer.data)