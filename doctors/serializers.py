from rest_framework import serializers
from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = [
            'id', 'created_by', 'name', 'email', 'specialization', 'license_number', 'phone', 'bio',
            'years_of_experience', 'qualifications', 'clinic_address',
            'clinic_city', 'clinic_state', 'clinic_zip', 'consultation_fee',
            'availability', 'is_verified', 'profile_picture', 'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_by', 'is_verified', 'created_at', 'updated_at']


class DoctorCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = [
            'name', 'email', 'specialization', 'license_number', 'phone', 'bio',
            'years_of_experience', 'qualifications', 'clinic_address',
            'clinic_city', 'clinic_state', 'clinic_zip', 'consultation_fee',
            'availability', 'profile_picture'
        ]
