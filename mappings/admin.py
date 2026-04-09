from django.contrib import admin
from mappings.models import PatientDoctorMapping, Consultation


@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ['get_patient', 'get_doctor', 'status', 'is_primary_doctor', 'assigned_date']
    list_filter = ['status', 'is_primary_doctor', 'assigned_date']
    search_fields = ['patient__user__email', 'doctor__user__email']
    readonly_fields = ['assigned_date', 'created_at', 'updated_at']
    
    def get_patient(self, obj):
        return f"{obj.patient.user.first_name} {obj.patient.user.last_name}"
    get_patient.short_description = 'Patient'
    
    def get_doctor(self, obj):
        return f"Dr. {obj.doctor.user.first_name} {obj.doctor.user.last_name}"
    get_doctor.short_description = 'Doctor'


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ['get_patient', 'get_doctor', 'consultation_type', 'status', 'scheduled_date']
    list_filter = ['consultation_type', 'status', 'scheduled_date']
    search_fields = ['mapping__patient__user__email', 'mapping__doctor__user__email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Mapping', {'fields': ('mapping',)}),
        ('Type & Status', {'fields': ('consultation_type', 'status')}),
        ('Dates', {'fields': ('scheduled_date', 'completed_date', 'next_followup')}),
        ('Medical Info', {'fields': ('notes', 'prescription')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def get_patient(self, obj):
        return f"{obj.mapping.patient.user.first_name} {obj.mapping.patient.user.last_name}"
    get_patient.short_description = 'Patient'
    
    def get_doctor(self, obj):
        return f"Dr. {obj.mapping.doctor.user.first_name} {obj.mapping.doctor.user.last_name}"
    get_doctor.short_description = 'Doctor'
