from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow users to manage their own mappings or admin to manage all."""
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.patient.user == request.user or obj.doctor.user == request.user
