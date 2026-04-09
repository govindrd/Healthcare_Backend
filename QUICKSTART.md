# Quick Start Guide - Healthcare Backend

##  Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
pip install djangorestframework-simplejwt
```

### Step 2: Create & Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create Superuser
```bash
python manage.py createsuperuser
# Enter email and password
```

### Step 4: Run Development Server
```bash
python manage.py runserver
```

### Step 5: Access Services

**Admin Panel**: http://localhost:8000/admin/
- User: (your superuser email)
- Password: (your password)

**API Documentation**: http://localhost:8000/api-docs/swagger/

## 📝 First API Call Example

### Register a New User
```bash
curl -X POST http://localhost:8000/api/v1/auth/register/ \
  -H "Content-Type: application/json" \
  -d {
    "email": "patient@example.com",
    "password": "securepass123",
    "password2": "securepass123",
    "first_name": "Govind",
    "last_name": "Rathod",
    "user_type": "patient",
    "phone": "+1234567890"
  }
```

**Response** (includes JWT tokens):
```json
{
  "user": {
    "id": 1,
    "email": "patient@example.com",
    "first_name": "Govind",
    "last_name": "Rathod",
    "user_type": "patient",
    "phone": "+1234567890"
  },
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login/ \
  -H "Content-Type: application/json" \
  -d {
    "email": "patient@example.com",
    "password": "securepass123"
  }
```

### Using JWT Token in Requests
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE" \
  http://localhost:8000/api/v1/auth/profile/
```

## 📚 Key User Types

### Patient
- Register with `user_type: "patient"`
- Create/update patient profile
- View assigned doctors
- Schedule consultations
- View medical history

### Doctor
- Register with `user_type: "doctor"`
- Create doctor profile with specialization
- View assigned patients
- Manage consultations
- Write prescriptions

### Admin
- Super user created via `createsuperuser` command
- Access Django admin panel
- Manage all users and records
- Verify doctor credentials

##  CORS Configuration

Default CORS allows:
- localhost:3000
- localhost:8000
- 127.0.0.1:3000

Edit `healthcare_backend/settings.py` to modify.

##  Important Files to Know

| File | Purpose |
|------|---------|
| `manage.py` | Django management script |
| `healthcare_backend/settings.py` | Main Django settings |
| `healthcare_backend/urls.py` | Main URL routing |
| `accounts/models.py` | Custom User model |
| `patients/models.py` | Patient data model |
| `doctors/models.py` | Doctor data model |
| `mappings/models.py` | Consultation & mapping models |
| `.env` | Environment variables (create this) |

##  Environment Variables

Create `.env` file in root:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

##  Run Tests

```bash
python manage.py test tests/
```

##  Database Schema

```
CustomUser (one-to-one with Django User)
├── Patient
├── Doctor
└── [Other user data]

PatientDoctorMapping
├── Patient (FK)
├── Doctor (FK)
└── Consultation (FK)

Consultation
├── PatientDoctorMapping (FK)
```

##  Common Issues

### Issue: `ModuleNotFoundError: No module named 'rest_framework'`
**Solution**: Run `pip install -r requirements.txt`

### Issue: `No such table: accounts_customuser`
**Solution**: Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: Port 8000 already in use
**Solution**: Use different port:
```bash
python manage.py runserver 8000
```

##  Next Steps

1.  Complete the 5-minute setup
2.  Test API endpoints in Swagger
3.  Design frontend UI
4.  Implement webhooks
5.  Setup production deployment

##  Support

Refer to `README.md` for complete documentation.

