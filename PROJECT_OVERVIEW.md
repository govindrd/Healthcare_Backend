# Healthcare Backend - Project Overview

## 📋 Project Summary

A comprehensive Django REST Framework backend for a healthcare management system. The project is designed with a modular architecture following Django best practices, enabling easy scaling and maintenance.

## 🎯 Core Modules

### 1. **Accounts Module** (`accounts/`)
- **Purpose**: User authentication and management
- **Components**:
  - `models.py`: CustomUser model with email authentication
  - `serializers.py`: User registration, login, password change
  - `views.py`: Auth endpoints (register, login, profile, change-password)
  - `permissions.py`: Role-based permissions (IsPatient, IsDoctor, IsAdmin)
  - `admin.py`: Django admin customization

**Models**:
```
CustomUser
├── is_patient/doctor/admin (user_type)
├── email (unique)
├── phone
├── is_verified
└── custom fields for user management
```

---

### 2. **Patients Module** (`patients/`)
- **Purpose**: Patient profile and medical history management
- **Components**:
  - `models.py`: Patient profile with medical information
  - `serializers.py`: Patient data serialization
  - `views.py`: CRUD operations for patient profiles
  - `permissions.py`: Patient-specific access control

**Models**:
```
Patient
├── user (OneToOne with CustomUser)
├── medical_history
├── allergies
├── emergency_contact
├── blood_group
└── contact_information
```

**Key Features**:
- Create/update patient profile
- View medical history
- Manage emergency contacts
- Track allergies

---

### 3. **Doctors Module** (`doctors/`)
- **Purpose**: Doctor profiles with specializations and availability
- **Components**:
  - `models.py`: Doctor profile with specializations
  - `serializers.py`: Doctor information serialization
  - `views.py`: Doctor listing and filtering
  - `permissions.py`: Doctor-specific permissions

**Models**:
```
Doctor
├── user (OneToOne with CustomUser)
├── specialization (Cardiology, Neurology, etc.)
├── license_number (unique)
├── experience_years
├── clinic_information
├── consultation_fee
├── is_verified
└── availability_schedule
```

**Key Features**:
- Doctor profile with qualifications
- Filter by specialization
- Manage consultation fees
- Track doctor verification status

---

### 4. **Mappings Module** (`mappings/`)
- **Purpose**: Patient-Doctor relationships and consultation management
- **Components**:
  - `models.py`: PatientDoctorMapping and Consultation models
  - `serializers.py`: Mapping and consultation serialization
  - `views.py`: APIs for managing relationships
  - `permissions.py`: Access control for mappings
  - `services.py`: Business logic and signal handlers

**Models**:
```
PatientDoctorMapping
├── patient (FK)
├── doctor (FK)
├── status (pending/approved/discontinued)
├── is_primary_doctor
└── assignment_notes

Consultation
├── mapping (FK to PatientDoctorMapping)
├── type (online/offline)
├── status (scheduled/completed/cancelled)
├── scheduled_date
├── notes
├── prescription
└── next_followup
```

**Key Features**:
- Assign doctors to patients
- Schedule consultations
- Track consultation history
- Write prescriptions
- Set follow-up appointments

---

### 5. **Common Module** (`common/`)
- **Purpose**: Shared utilities and helper functions
- **Components**:
  - `permissions.py`: Shared permission classes
  - `pagination.py`: Custom pagination for paginated responses
  - `responses.py`: Standard API response format
  - `utils.py`: Helper functions (ID generation, slugs, etc.)

**Key Features**:
- Consistent API response format
- Pagination support
- Utility functions for common operations
- Shared permission classes

**Response Format**:
```json
{
  "status": "success|error",
  "message": "Operation message",
  "data": {},
  "pagination": {
    "count": 100,
    "next": "...",
    "previous": "...",
    "page_size": 20,
    "total_pages": 5
  }
}
```

---

### 6. **Config Module** (`config/`)
- **Purpose**: Environment-based configuration
- **Files**:
  - `settings/base.py`: Base settings shared across environments
  - `settings/dev.py`: Development-specific settings
  - `settings/prod.py`: Production-specific settings

**Usage**:
```bash
# Development
export DJANGO_SETTINGS_MODULE=config.settings.dev
python manage.py runserver

# Production
export DJANGO_SETTINGS_MODULE=config.settings.prod
gunicorn healthcare_backend.wsgi
```

---

### 7. **Tests Module** (`tests/`)
- **Purpose**: Unit and integration tests
- **Files**:
  - `test_auth.py`: Authentication tests
  - `test_patients.py`: Patient endpoint tests
  - `test_doctors.py`: Doctor endpoint tests

**Running Tests**:
```bash
python manage.py test tests/
python manage.py test tests.test_auth
```

---

##  Module Dependencies

```
accounts (Base)
├── CustomUser model
├── Permissions
└── Authenticators

patients (Depends on accounts)
├── Uses CustomUser
├── References to Doctors (in consultations)
└── Permissions from accounts

doctors (Depends on accounts)
├── Uses CustomUser
├── Referenced by Patients
└── Permissions from accounts

mappings (Depends on patients & doctors)
├── Connects Patient & Doctor
├── Uses PatientDoctorMapping
├── Uses Consultation
└── Permissions from accounts

common (Utility)
├── Used by all modules
├── Pagination
├── Response formatting
└── Shared permissions
```

---

##  API Structure

```
/api/v1/
├── /auth/
│   ├── register/ (POST)
│   ├── login/ (POST)
│   ├── profile/ (GET, PUT)
│   ├── change-password/ (POST)
│   └── users/ (ViewSet)
│
├── /patients/
│   ├── (GET, POST, PUT, DELETE)
│   └── my_profile/ (GET)
│
├── /doctors/
│   ├── (GET, POST, PUT, DELETE)
│   ├── my_profile/ (GET)
│   └── by_specialization/ (GET with filter)
│
└── /mappings/
    ├── mappings/
    │   ├── (GET, POST, PUT, DELETE)
    │   ├── my_doctors/ (GET)
    │   └── my_patients/ (GET)
    │
    └── consultations/
        ├── (GET, POST, PUT, DELETE)
        ├── upcoming/ (GET)
        └── completed/ (GET)
```

---

##  Authentication Flow

```
1. User registers at /api/v1/auth/register/
   └── Creates CustomUser with user_type
   
2. System creates JWT tokens
   └── access_token (short-lived)
   └── refresh_token (long-lived)

3. User includes token in requests
   ├── Header: Authorization: Bearer <access_token>
   └── API validates user and user_type

4. Permission classes check user_type
   ├── IsPatient
   ├── IsDoctor
   ├── IsAdmin
   └── Custom logic
```

---

##  Data Flow Example

```
Patient Registration Flow:
1. User calls POST /api/v1/auth/register/
   └── UserManager.create_user()
   └── Creates CustomUser(user_type='patient')
   └── Returns JWT tokens

2. User calls POST /api/v1/patients/
   └── PatientViewSet.create()
   └── perform_create() sets user=request.user
   └── Creates Patient record

3. User calls GET /api/v1/mappings/
   └── get_queryset() filters by user_type
   └── Returns doctor assignments

Doctor Assignment Flow:
1. Admin calls POST /api/v1/mappings/mappings/
   └── Creates PatientDoctorMapping
   └── Signals notify about new mapping

2. Consultation scheduled:
   └── POST /api/v1/mappings/consultations/
   └── Links consultation to mapping

3. Consultation completed:
   └── PUT /api/v1/mappings/consultations/{id}/
   └── Updates status, adds notes & prescription
```

---

## 🛠 Technology Stack

- **Framework**: Django 4.2.0
- **API**: Django REST Framework 3.14.0
- **Authentication**: JWT (Simple JWT)
- **Database**: SQLite (dev), PostgreSQL (prod)
- **Documentation**: drf-yasg (Swagger/ReDoc)
- **CORS**: django-cors-headers
- **Image handling**: Pillow
- **Environment**: python-decouple
- **Async**: Daphne (ASGI server)
- **Task Queue**: Celery (optional)

---
