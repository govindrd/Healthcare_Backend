from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow users to edit their own patient profile only."""
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsPatient(permissions.BasePermission):
    """Allow access only to patients."""
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'patient')
