from rest_framework import viewsets, filters
from .models import Task
from .serializer import TaskSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Lower
from rest_framework import generics


class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class= TaskSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner= self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

    filter_backends= [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]
    filterset_fields= ['is_done']
    search_fields= ['title', 'description']
    ordering_fields= ['id', 'title', 'is_done']


class RegisterView(generics.CreateAPIView):
    serializer_class= UserRegisterSerializer