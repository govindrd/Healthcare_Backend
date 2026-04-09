from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow doctor to edit their own profile or admin to manage all."""
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsDoctor(permissions.BasePermission):
    """Allow access only to doctors."""
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.user_type == 'doctor')
