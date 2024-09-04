from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' and request.user.is_staff:
            return True
        return obj.created_by == request.user
