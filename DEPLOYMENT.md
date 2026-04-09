# Deployment Guide

This guide covers deploying the Healthcare Backend to various platforms.

## Prerequisites

- Docker & Docker Compose installed
- GitHub repository created
- Cloud account (for production deployment)

## Local Development with Docker

### Quick Start
```bash
# Start all services
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access the application
# Django: http://localhost:8000
# Postgres: localhost:5432
# Redis: localhost:6379
```

### Stop Services
```bash
docker-compose down
```

### View Logs
```bash
docker-compose logs -f web
```

## Production Deployment

### Environment Variables Setup

Create `.env.production` with production values:
```env
DEBUG=False
SECRET_KEY=your-strong-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_ENGINE=django.db.backends.postgresql
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-strong-password
DB_HOST=db-host
DB_PORT=5432
REDIS_URL=redis://redis-host:6379/0
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Railway Deployment (Recommended)

1. **Connect GitHub Repository:**
   - Go to [https://railway.app](https://railway.app)
   - Sign in with GitHub
   - Create new project
   - Select "Deploy from GitHub repo"
   - Choose `healthcare_backend` repository

2. **Configure Environment:**
   - Add variables from `.env.production`
   - Railway auto-generates PostgreSQL database
   - Add Redis add-on for Celery tasks

3. **Configure Build & Start:**
   - Build command: Leave empty (auto-detected)
   - Start command: `gunicorn healthcare_backend.wsgi:application`

4. **Domain Configuration:**
   - Railway provides free domain
   - Or connect custom domain in settings
   - Configure ALLOWED_HOSTS

5. **Deploy:**
   - Push to main branch triggers auto-deploy
   - Monitor deployment in Railway dashboard

### Heroku Deployment

```bash
# Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# Login
heroku login

# Create app
heroku create healthcare-backend-app

# Add PostgreSQL add-on
heroku addons:create heroku-postgresql:standard-0

# Add Redis add-on (for Celery)
heroku addons:create heroku-redis:premium-0

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
heroku config:set ALLOWED_HOSTS=healthcare-backend-app.herokuapp.com
heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
heroku config:set EMAIL_HOST=smtp.gmail.com
heroku config:set EMAIL_PORT=587
heroku config:set EMAIL_HOST_USER=your-email@gmail.com
heroku config:set EMAIL_HOST_PASSWORD=your-app-password

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# View logs
heroku logs -t
```

### AWS ECS Deployment

1. **Create ECR Repository:**
```bash
aws ecr create-repository \
  --repository-name healthcare-backend \
  --region us-east-1
```

2. **Build and Push Image:**
```bash
aws ecr get-login-password --region us-east-1 | \
  docker login --username AWS --password-stdin \
  YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

docker build -t healthcare-backend:latest .

docker tag healthcare-backend:latest \
  YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/healthcare-backend:latest

docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/healthcare-backend:latest
```

3. **Create ECS Cluster and Task Definition:**
   - Use AWS Console or AWS CLI
   - Reference: [AWS ECS Documentation](https://docs.aws.amazon.com/ecs/)

4. **Setup RDS Database:**
   - Create PostgreSQL RDS instance
   - Configure security groups for ECS access

5. **Create ElastiCache Redis:**
   - For Celery tasks
   - Same VPC as ECS tasks

### Google Cloud Run Deployment

```bash
# Build with Cloud Build
gcloud builds submit --tag gcr.io/YOUR_PROJECT/healthcare-backend

# Deploy to Cloud Run
gcloud run deploy healthcare-backend \
  --image gcr.io/YOUR_PROJECT/healthcare-backend \
  --platform managed \
  --region us-central1 \
  --set-env-vars DEBUG=False,SECRET_KEY=your-key

# Setup Cloud SQL for PostgreSQL
# Setup Cloud Memorystore for Redis
```

## Post-Deployment Checklist

- [ ] Run migrations: `python manage.py migrate`
- [ ] Create superuser: `python manage.py createsuperuser`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Test API endpoints
- [ ] Configure email backend
- [ ] Setup logging and monitoring
- [ ] Configure backups for database
- [ ] Setup SSL/TLS certificate
- [ ] Configure CDN for static files (optional)
- [ ] Monitor with application monitoring tool

## Monitoring & Logging

### Application Monitoring
- Use New Relic, Datadog, or Sentry
- Monitor performance metrics
- Track error rates

### Log Aggregation
- Use CloudWatch, Stackdriver, or ELK
- Store logs for debugging
- Set up alerts

### Database Backups
- Set up automated backups
- Test restore procedures
- Maintain backup retention policy

## Scaling

### Horizontal Scaling
- Add more application instances
- Use load balancer (ALB, NLB)
- Database read replicas for scaling reads

### Caching
- Redis for session storage
- Redis for Celery task queue
- CDN for static files

### Database Optimization
- Add database indexes
- Use connection pooling
- Monitor slow queries

## Security Checklist

- [ ] Use strong SECRET_KEY
- [ ] Set DEBUG=False in production
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Use HTTPS/TLS
- [ ] Enable CORS properly
- [ ] Implement rate limiting
- [ ] Secure sensitive environment variables
- [ ] Regular security updates
- [ ] Database encryption
- [ ] Regular backups

## Troubleshooting

### Common Issues

**502 Bad Gateway:**
- Check if application is running
- Check logs for errors
- Verify database connectivity

**Static Files Not Loading:**
- Run `python manage.py collectstatic`
- Check STATIC_URL and STATIC_ROOT
- Verify web server configuration

**Database Connection Issues:**
- Verify connection string
- Check database is accessible
- Verify firewall rules

**Celery Tasks Not Running:**
- Verify Redis/RabbitMQ connection
- Check Celery worker logs
- Verify task is registered

## Support & Help

- GitHub Issues: Report bugs and request features
- Documentation: Check README and guides
- Community: Join discussions

## References

- [Django Deployment Guide](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Railway Documentation](https://docs.railway.app/)
- [Heroku Django Guide](https://devcenter.heroku.com/articles/django-app-configuration)
- [AWS ECS](https://docs.aws.amazon.com/ecs/)
- [Google Cloud Run](https://cloud.google.com/run/docs)
