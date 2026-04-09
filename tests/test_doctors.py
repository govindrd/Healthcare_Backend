from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from accounts.models import CustomUser
from doctors.models import Doctor


class DoctorTestCase(TestCase):
    """Test cases for doctor management"""
    
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='doctor@example.com',
            password='testpass123',
            user_type='doctor'
        )
        self.client.force_authenticate(user=self.user)
        self.list_url = reverse('doctor-list')
        
    def test_create_doctor_profile(self):
        """Test creating a doctor profile"""
        data = {
            'user': self.user.id,
            'specialization': 'Cardiology',
            'license_number': 'DOC123456',
            'phone': '+1234567890',
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_list_doctors(self):
        """Test listing doctors"""
        Doctor.objects.create(
            user=self.user,
            specialization='Cardiology',
            license_number='DOC123456',
            phone='+1234567890'
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
