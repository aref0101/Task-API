from rest_framework import viewsets, filters
from .models import Task
from .serializer import TaskSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .custom_permission import MyCustomPermission
from django.db.models.functions import Lower
from rest_framework import generics


class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all().annotate(lower_title= Lower('title'))
    serializer_class= TaskSerializer
    permission_classes= [IsAuthenticatedOrReadOnly, MyCustomPermission]

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

    filter_backends= [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    filterset_fields= ['is_done']
    search_fields= ['title', 'description']
    ordering_fields= ['id', 'lower_title', 'is_done']


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer