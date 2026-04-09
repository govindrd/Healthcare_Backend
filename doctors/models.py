from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Doctor(models.Model):
    """Doctor model"""
    SPECIALIZATIONS = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('Dermatology', 'Dermatology'),
        ('Psychiatry', 'Psychiatry'),
        ('General', 'General Practitioner'),
        ('Oncology', 'Oncology'),
        ('Gynecology', 'Gynecology'),
        ('Surgery', 'General Surgery'),
    ]
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_doctors', null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS)
    license_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    years_of_experience = models.IntegerField(default=0)
    qualifications = models.TextField(blank=True)
    clinic_address = models.TextField(blank=True)
    clinic_city = models.CharField(max_length=100, blank=True)
    clinic_state = models.CharField(max_length=100, blank=True)
    clinic_zip = models.CharField(max_length=20, blank=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    availability = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='doctors/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Dr. {self.name}"
    
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['-created_at']
