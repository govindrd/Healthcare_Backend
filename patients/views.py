from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from patients.models import Patient
from patients.serializers import PatientSerializer, PatientCreateUpdateSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """ViewSet for patient management"""
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PatientCreateUpdateSerializer
        return PatientSerializer
    
    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, user=self.request.user)
