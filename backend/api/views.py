from rest_framework import viewsets, filters
from .models import Task
from .serializer import TaskSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .custom_permission import MyCustomPermission


class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
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
    ordering_fields= ['id', 'title', 'is_done']