from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from patients.models import Patient


class PatientTestCase(TestCase):
    """Test cases for patient management"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='patient@example.com',
            password='testpass123',
            user_type='patient'
        )
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('patient-list')
        
    def test_create_patient_profile(self):
        """Test creating a patient profile"""
        data = {
            'user': self.user.id,
            'phone': '+1234567890',
            'date_of_birth': '1990-01-01',
            'medical_history': 'No significant history',
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_patients(self):
        """Test listing patients"""
        Patient.objects.create(
            user=self.user,
            phone='+1234567890',
            date_of_birth='1990-01-01'
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
