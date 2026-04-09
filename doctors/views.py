from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer, DoctorCreateUpdateSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    """ViewSet for doctor management"""
    queryset = Doctor.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return DoctorCreateUpdateSerializer
        return DoctorSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
