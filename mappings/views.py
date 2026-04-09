from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mappings.models import PatientDoctorMapping
from mappings.serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    """ViewSet for patient-doctor mapping"""
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.all()
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>\d+)')
    def by_patient(self, request, patient_id=None):
        """Get all doctors assigned to a specific patient"""
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
