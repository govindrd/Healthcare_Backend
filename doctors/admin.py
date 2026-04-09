from django.contrib import admin
from doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'specialization', 'license_number', 'is_verified', 'created_at']
    list_filter = ['specialization', 'is_verified', 'created_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'license_number']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Info', {'fields': ('user',)}),
        ('Professional', {'fields': ('specialization', 'license_number', 'years_of_experience', 'qualifications')}),
        ('Contact', {'fields': ('phone',)}),
        ('Clinic', {'fields': ('clinic_address', 'clinic_city', 'clinic_state', 'clinic_zip')}),
        ('Bio & Availability', {'fields': ('bio', 'availability')}),
        ('Consultation', {'fields': ('consultation_fee',)}),
        ('Profile', {'fields': ('profile_picture', 'is_verified')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def get_name(self, obj):
        return f"Dr. {obj.user.first_name} {obj.user.last_name}"
    get_name.short_description = 'Doctor Name'
