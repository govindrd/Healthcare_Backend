from rest_framework import serializers
from mappings.models import PatientDoctorMapping, Consultation
from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id', 'patient', 'doctor', 'patient_details', 'doctor_details',
            'status', 'assigned_date', 'notes', 'is_primary_doctor', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'assigned_date', 'created_at', 'updated_at']


class ConsultationSerializer(serializers.ModelSerializer):
    mapping_details = PatientDoctorMappingSerializer(source='mapping', read_only=True)
    
    class Meta:
        model = Consultation
        fields = [
            'id', 'mapping', 'mapping_details', 'consultation_type', 'status',
            'scheduled_date', 'completed_date', 'notes', 'prescription',
            'next_followup', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'completed_date', 'created_at', 'updated_at']
