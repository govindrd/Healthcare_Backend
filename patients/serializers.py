from rest_framework import serializers
from patients.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = [
            'id', 'created_by', 'name', 'email', 'phone', 'date_of_birth', 'gender', 'blood_group',
            'address', 'city', 'state', 'zip_code', 'medical_history',
            'allergies', 'emergency_contact', 'emergency_contact_phone',
            'profile_picture', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']


class PatientCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = [
            'name', 'email', 'phone', 'date_of_birth', 'gender', 'blood_group',
            'address', 'city', 'state', 'zip_code', 'medical_history',
            'allergies', 'emergency_contact', 'emergency_contact_phone',
            'profile_picture'
        ]
