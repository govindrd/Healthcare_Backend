from django.db import models
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    """Model to map patients with doctors"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('discontinued', 'Discontinued'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctors')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    assigned_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    is_primary_doctor = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('patient', 'doctor')
        verbose_name = 'Patient-Doctor Mapping'
        verbose_name_plural = 'Patient-Doctor Mappings'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.patient.name} - Dr. {self.doctor.name} ({self.status})"


class Consultation(models.Model):
    """Consultation model for doctor-patient interactions"""
    CONSULTATION_TYPE = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    mapping = models.ForeignKey(PatientDoctorMapping, on_delete=models.CASCADE, related_name='consultations')
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    scheduled_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    prescription = models.TextField(blank=True)
    next_followup = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'
        ordering = ['-scheduled_date']
    
    def __str__(self):
        return f"Consultation - {self.mapping.patient.user.email} with Dr. {self.mapping.doctor.user.first_name}"
