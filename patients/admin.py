from django.contrib import admin
from patients.models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'phone', 'date_of_birth', 'gender', 'blood_group', 'created_at']
    list_filter = ['gender', 'blood_group', 'created_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Info', {'fields': ('user',)}),
        ('Contact', {'fields': ('phone', 'emergency_contact', 'emergency_contact_phone')}),
        ('Personal', {'fields': ('date_of_birth', 'gender', 'blood_group', 'profile_picture')}),
        ('Address', {'fields': ('address', 'city', 'state', 'zip_code')}),
        ('Medical', {'fields': ('medical_history', 'allergies')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    
    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_name.short_description = 'Patient Name'
