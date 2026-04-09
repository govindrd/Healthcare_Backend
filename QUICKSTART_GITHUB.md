# Quick Start: Push to GitHub

Follow these steps to push your Healthcare Backend to GitHub.

## Step 1: Setup Git (One-time)

Open PowerShell and run:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

## Step 2: Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Enter Repository name: `healthcare_backend`
3. Enter Description: `Healthcare Backend API with Django, Docker, and JWT Authentication`
4. Choose **Public** (or Private if preferred)
5. **DO NOT** check "Initialize this repository with a README"
6. Click **Create repository**

## Step 3: Push Code to GitHub

Open PowerShell in the project directory:
```powershell
cd "c:\Users\Govind Rathod\Documents\healthcare_backend"
```

Run these commands in order:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Healthcare Backend API with Docker support, JWT authentication, and PostgreSQL"

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/healthcare_backend.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Expected Output

After the last command, you should see:
```
Enumerating objects: ...
Counting objects: ...
Compressing objects: ...
Writing objects: ...
...
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## Step 4: Verify

1. Go to [https://github.com/YOUR_USERNAME/healthcare_backend](https://github.com/YOUR_USERNAME/healthcare_backend)
2. Verify all files are uploaded
3. Check that README.md is displayed

## What Got Pushed?

Your GitHub repository now contains:
- ✅ Django application code
- ✅ Models and API endpoints
- ✅ Docker configuration (Dockerfile, docker-compose.yml)
- ✅ Postman collection for testing
- ✅ Environment configuration template (.env.example)
- ✅ GitHub Actions CI/CD workflow (.github/workflows/django-tests.yml)
- ✅ Contributing guidelines (.github/CONTRIBUTING.md)
- ✅ Issue templates (.github/ISSUE_TEMPLATE/)
- ✅ Deployment guides (DEPLOYMENT.md, README.md)
- ✅ Tests and documentation

## Next Steps

### Option 1: Enable GitHub Actions (CI/CD)
1. Go to **Actions** tab in your GitHub repository
2. Click **I understand my workflows, go ahead and enable them**
3. Tests will run automatically on push!

### Option 2: Deploy to Production (Choose One)

**Railway** (Easiest - Recommended):
1. Go to [https://railway.app](https://railway.app)
2. Sign in with GitHub
3. Select **Deploy from GitHub repo**
4. Choose `healthcare_backend`
5. Add environment variables
6. Deploy! (auto-deploys on push to main)

**Heroku**:
```powershell
# Install Heroku CLI first
heroku login
heroku create healthcare-backend-app
git push heroku main
```

**Render**:
1. Go to [https://render.com](https://render.com)
2. Connect GitHub account
3. Deploy!

## Troubleshooting

### "fatal: not a git repository"
Solution: Make sure you're in the correct directory:
```powershell
cd "c:\Users\Govind Rathod\Documents\healthcare_backend"
```

### "fatal: Could not read from remote repository"
Solution: Replace `YOUR_USERNAME` with your actual GitHub username:
```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/healthcare_backend.git
```

### "Permission denied (publickey)"
Solution: Setup SSH key or use HTTPS with personal access token:
```powershell
git remote set-url origin https://github.com/YOUR_USERNAME/healthcare_backend.git
git config --global user.password "your-github-token"
```

### Files already committed?
You can sync any changes with:
```powershell
git add .
git commit -m "Your commit message"
git push
```

## Support

If you encounter any issues:
1. Check [GitHub status](https://www.githubstatus.com/)
2. Verify your GitHub account has write access
3. Check [GitHub documentation](https://docs.github.com/)
4. Open an issue in your repository

---

**Congratulations!** Your Healthcare Backend is now on GitHub! 🎉
