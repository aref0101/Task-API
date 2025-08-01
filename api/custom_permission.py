from rest_framework.permissions import BasePermission

class MyCustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in('PUT', 'DELETE', 'PATCH'):
            return obj.owner== request.user
        return True