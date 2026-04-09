# Healthcare Backend API

A comprehensive Django REST Framework backend for a healthcare management system supporting patient-doctor interactions, consultations, and medical records management.

## Quick Links

- 🚀 [Push to GitHub](./QUICKSTART_GITHUB.md) - Step-by-step guide to push code
- 🐳 [Docker Setup](./README.md#docker-setup) - Run with Docker Compose
- 📘 [Deployment Guide](./DEPLOYMENT.md) - Deploy to production
- 🤝 [Contributing Guide](./.github/CONTRIBUTING.md) - How to contribute
- 📝 [API Documentation](#api-documentation) - Available endpoints

## Project Structure

```
healthcare_backend/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Project dependencies
├── .env                               # Environment variables
├── .gitignore                         # Git ignore file
│
├── healthcare_backend/                # Main project config
│   ├── __init__.py
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL routing
│   ├── asgi.py                        # ASGI configuration
│   └── wsgi.py                        # WSGI configuration
│
├── accounts/                          # Authentication & User Management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py                       # Admin customization
│   ├── apps.py
│   ├── models.py                      # Custom User Model
│   ├── serializers.py                 # Register/Login Serializer
│   ├── views.py                       # Auth APIs
│   ├── urls.py                        # App URL routing
│   └── permissions.py                 # Auth-related permissions
│
├── patients/                          # Patient Management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Patient Model
│   ├── serializers.py
│   ├── views.py                       # Patient APIs
│   ├── urls.py
│   └── permissions.py                 # Patient-specific permissions
│
├── doctors/                           # Doctor Management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Doctor Model with specializations
│   ├── serializers.py
│   ├── views.py                       # Doctor APIs
│   ├── urls.py
│   └── permissions.py                 # Doctor-specific permissions
│
├── mappings/                          # Patient-Doctor Mapping & Consultations
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # PatientDoctorMapping & Consultation Models
│   ├── serializers.py
│   ├── views.py                       # Mapping & Consultation APIs
│   ├── urls.py
│   ├── permissions.py
│   └── services.py                    # Business logic & signal handlers
│
├── common/                            # Shared Utilities (BEST PRACTICE)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py                 # Shared permission classes
│   ├── pagination.py                  # Custom pagination
│   ├── responses.py                   # Standard API responses
│   ├── utils.py                       # Helper functions
│   └── urls.py
│
├── config/                            # Advanced Configuration
│   ├── __init__.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py                    # Base settings
│       ├── dev.py                     # Development settings
│       └── prod.py                    # Production settings
│
└── tests/                             # Unit & Integration Tests
    ├── __init__.py
    ├── test_auth.py
    ├── test_patients.py
    └── test_doctors.py
```

## Installation & Setup

### 1. Prerequisites
- Python 3.9+
- pip 
- Virtual environment (recommended)

### 2. Create Virtual Environment
```bash
python -m venv env

# Activate the virtual environment:
# On Linux/Mac:
source env/bin/activate

# On Windows (PowerShell):
env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory for PostgreSQL:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5431

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000/admin/` to access the Django admin panel.

## Docker Setup

### Prerequisites
- Docker
- Docker Compose

### Environment Variables
Copy `.env.example` to `.env` and update values:
```bash
cp .env.example .env
```

### Build and Run with Docker Compose
```bash
# Build images
docker-compose build

# Start all services (PostgreSQL, Redis, Django, Celery)
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput
```

### Services Running
- **Django**: `http://localhost:8000`
- **PostgreSQL**: `localhost:5432` (host: db)
- **Redis**: `localhost:6379` (host: redis)
- **Celery Worker**: Running in background

### Stop Services
```bash
docker-compose down
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
```

### Access Django Shell
```bash
docker-compose exec web python manage.py shell
```

## API Documentation

API documentation is available at:
- **Swagger UI**: `http://localhost:8000/api-docs/swagger/`
- **ReDoc**: `http://localhost:8000/api-docs/redoc/`
- **OpenAPI Schema**: `http://localhost:8000/api-docs/schema.json`

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `GET /api/auth/profile/` - Get user profile
- `PUT /api/auth/profile/` - Update user profile
- `POST /api/auth/change-password/` - Change password

### Patients
- `GET /api/patients/` - List all your patients
- `POST /api/patients/` - Create patient
- `GET /api/patients/{id}/` - Get patient details
- `PUT /api/patients/{id}/` - Update patient
- `DELETE /api/patients/{id}/` - Delete patient

### Doctors
- `GET /api/doctors/` - List all doctors (public)
- `POST /api/doctors/` - Create doctor (authenticated)
- `GET /api/doctors/{id}/` - Get doctor details
- `PUT /api/doctors/{id}/` - Update doctor
- `DELETE /api/doctors/{id}/` - Delete doctor

### Mappings
- `GET /api/mappings/` - List patient-doctor mappings
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/patient/{patient_id}/` - Get doctors for patient
- `DELETE /api/mappings/{id}/` - Remove mapping

## Database Models

### CustomUser
Extended Django User model with:
- Email-based authentication
- User type (patient/doctor/admin)
- Phone number
- Email verification status
- Timestamps

### Patient
Patient profile with:
- One-to-one relationship with CustomUser
- Medical history
- Contact information
- Emergency contact
- Blood group & allergies
- Profile picture

### Doctor
Doctor profile with:
- Specializations
- License number
- Years of experience
- Clinic information
- Consultation fees
- Verification status
- Availability

### PatientDoctorMapping
Links patients with doctors:
- Assignment status (pending/approved/discontinued)
- Primary doctor designation
- Assignment notes
- Timestamps

### Consultation
Manages doctor-patient consultations:
- Consultation type (online/offline)
- Status tracking
- Scheduling information
- Medical notes & prescriptions
- Follow-up scheduling

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in requests:

```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:8000/api/patients/
```

## Example Requests

### 1. Register User
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123",
    "password2": "SecurePass123",
    "first_name": "John",
    "last_name": "Doe",
    "user_type": "patient",
    "phone": "1234567890"
  }'
```

### 2. Login
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "SecurePass123"}'
```

### 3. Add Patient
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "1234567890",
    "date_of_birth": "1990-01-01",
    "gender": "F",
    "blood_group": "O+",
    "address": "123 Main St",
    "city": "Mumbai",
    "state": "Maharashtra",
    "zip_code": "400001",
    "medical_history": "No major issues",
    "allergies": "Pollen",
    "emergency_contact": "John Doe",
    "emergency_contact_phone": "0987654321"
  }'
```

### 4. Get Patients
```bash
curl -X GET http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer <access_token>"
```

## Testing with Postman

### 1. Import the Postman Collection

1. Open Postman
2. Click **File** → **Import**
3. Select the file: `Assignment_Postman_Collection.postman_collection.json`
4. The collection will be imported with all pre-configured requests

### 2. Set Up Environment Variables

1. Create a new environment in Postman:
   - Click **Environments** (gear icon) → **Create Environment**
   - Name it: `Healthcare Backend`

2. Add these variables:
   - `base_url`: `http://127.0.0.1:8000`
   - `access_token`: (leave empty for now, will be populated after login)

3. Select the environment: Click the environment dropdown and select `Healthcare Backend`

### 3. Testing Workflow

#### Step 1: Register a User
1. Open **Authentication APIs** → **POST /api/auth/register/**
2. Click **Send**
3. Response should return `201 Created` with user details and tokens

#### Step 2: Login
1. Open **Authentication APIs** → **POST /api/auth/login/**
2. Body should have your registered email and password
3. Click **Send**
4. Copy the `access` token from the response
5. Set the Postman environment variable:
   - Go to **Environments** → Select your environment
   - Paste the token into the `access_token` variable
   - Click **Save**

#### Step 3: Create a Patient
1. Open **Patient Management APIs** → **POST /api/patients/**
2. Verify headers include:
   - `Authorization: Bearer {{access_token}}`
   - `Content-Type: application/json`
3. Update the body with patient details (name, email, phone, etc.)
4. Click **Send**
5. Response should return `201 Created` with patient ID

#### Step 4: View Patients
1. Open **Patient Management APIs** → **GET /api/patients/**
2. Headers should automatically include the Bearer token
3. Click **Send**
4. Returns list of patients created by the logged-in user

#### Step 5: Create a Doctor
1. Open **Doctor Management APIs** → **POST /api/doctors/**
2. Add doctor details (name, email, specialization, license_number, etc.)
3. Click **Send**
4. Response returns `201 Created` with doctor ID

#### Step 6: Create a Patient-Doctor Mapping
1. Open **Patient-Doctor Mapping APIs** → **POST /api/mappings/**
2. Body:
   ```json
   {
     "patient": 1,
     "doctor": 1,
     "status": "approved",
     "notes": "Primary care physician"
   }
   ```
3. Click **Send**
4. Response returns the mapping with `201 Created`

#### Step 7: View Patient's Doctors
1. Open **Patient-Doctor Mapping APIs** → **GET /api/mappings/patient/<patient_id>/**
2. Replace `<patient_id>` with the actual patient ID (e.g., `1`)
3. Click **Send**
4. Returns list of doctors assigned to that patient

### Tips

- **Use Bearer Token**: After login, the `{{access_token}}` variable is automatically injected
- **Check Headers**: Ensure `Authorization: Bearer {{access_token}}` is in the Headers tab
- **Update IDs**: Replace `<id>` placeholders with actual resource IDs from previous responses
- **Postman Tests**: Use the **Tests** tab in Postman to automatically extract tokens:
  ```javascript
  var jsonData = pm.response.json();
  pm.environment.set("access_token", jsonData.access);
  ```

## Running Tests

```bash
python manage.py test tests/
```

## Production Deployment

1. Update `.env` with production settings
2. Set `DEBUG=False`
3. Configure allowed hosts
4. Use PostgreSQL or production database
5. Set up proper email backend
6. Use environment-specific settings from `config/settings/prod.py`

## Dependencies

- Django 4.2.0
- Django REST Framework 3.14.0
- django-cors-headers 4.0.0
- python-decouple 3.8
- PyJWT 2.6.0
- Pillow 9.5.0
- drf-yasg 1.21.5
- djangorestframework-simplejwt (for JWT)
- Gunicorn 21.2.0
- Celery 5.2.7
- Redis 4.5.5

## GitHub & Deployment

### Step 1: Setup Git Locally

Configure your Git identity (if not already done):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 2: Initialize Repository & Push to GitHub

1. **Navigate to project directory:**
   ```bash
   cd "c:\Users\Govind Rathod\Documents\healthcare_backend"
   ```

2. **Initialize Git repository:**
   ```bash
   git init
   ```

3. **Add all files to staging:**
   ```bash
   git add .
   ```

4. **Create initial commit:**
   ```bash
   git commit -m "Initial commit: Healthcare Backend API with Docker support, JWT authentication, and PostgreSQL"
   ```

5. **Create GitHub repository:**
   - Go to [https://github.com/new](https://github.com/new)
   - Repository name: `healthcare_backend`
   - Description: "Healthcare Backend API with Django, Docker, and JWT Authentication"
   - Choose Public or Private
   - **Do NOT** initialize with README (we already have one)
   - Click **Create repository**

6. **Add remote and push:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/healthcare_backend.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Add GitHub Actions (Optional CI/CD)

Create `.github/workflows/django-tests.yml`:
```yaml
name: Django Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15-alpine
        env:
          POSTGRES_DB: healthcare_db
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run migrations
      run: python manage.py migrate
    
    - name: Run tests
      run: python manage.py test tests/
```

### Docker Image for Production

Build and push Docker image to Docker Hub:

1. **Create Docker Hub account:** [https://hub.docker.com](https://hub.docker.com)

2. **Login to Docker Hub:**
   ```bash
   docker login
   ```

3. **Build image:**
   ```bash
   docker build -t your-username/healthcare-backend:latest .
   ```

4. **Push to Docker Hub:**
   ```bash
   docker push your-username/healthcare-backend:latest
   ```


This project is licensed under the MIT License.

## Support

For issues and questions, open an issue on GitHub or contact the maintainers.

