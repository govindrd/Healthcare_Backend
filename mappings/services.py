from django.db.models.signals import post_save
from django.dispatch import receiver
from mappings.models import PatientDoctorMapping


@receiver(post_save, sender=PatientDoctorMapping)
def update_patient_doctor_on_mapping(sender, instance, created, **kwargs):
    """Signal to track mapping creation"""
    if created:
        print(f"New mapping created: {instance.patient.user.email} with Dr. {instance.doctor.user.first_name}")
