#!/usr/bin/env python3
"""
Comprehensive Render Deployment Script for Django Portfolio
This script prepares your Django portfolio for deployment on Render.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_step(step, description):
    """Print a formatted step"""
    print(f"\n📋 Step {step}: {description}")
    print("-" * 50)

def run_command(command, description, check=True):
    """Run a shell command and handle errors"""
    print(f"   Running: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ {description} completed successfully")
            return result.stdout
        else:
            print(f"   ❌ {description} failed")
            print(f"   Error: {result.stderr}")
            if check:
                sys.exit(1)
            return None
    except Exception as e:
        print(f"   ❌ Error running command: {e}")
        if check:
            sys.exit(1)
        return None

def check_prerequisites():
    """Check if all prerequisites are met"""
    print_header("Checking Prerequisites")
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        sys.exit(1)
    
    # Check if Django is installed
    try:
        import django
        print(f"✅ Django {django.get_version()} is installed")
    except ImportError:
        print("❌ Django is not installed")
        sys.exit(1)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ manage.py not found. Please run this script from the project root.")
        sys.exit(1)
    
    print("✅ All prerequisites met!")

def setup_environment():
    """Set up environment variables and configuration"""
    print_header("Setting Up Environment")
    
    # Create .env file for local development
    env_content = """# Django Settings
DEBUG=False
SECRET_KEY=your-secret-key-here-change-in-production
ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com

# Database (SQLite for local, PostgreSQL for production)
DATABASE_URL=sqlite:///db.sqlite3

# Email Settings (configure for production)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=vijaypardhu17@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here

# Static Files
STATIC_URL=/static/
MEDIA_URL=/media/
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file for local development")
    
    # Create production .env file
    prod_env_content = """# Production Environment Variables
DEBUG=False
SECRET_KEY=change-this-in-render-dashboard
ALLOWED_HOSTS=.onrender.com
DATABASE_URL=postgres://user:pass@host:port/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=vijaypardhu17@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
"""
    
    with open('.env.production', 'w') as f:
        f.write(prod_env_content)
    
    print("✅ Created .env.production file")

def update_render_config():
    """Update render.yaml with current project settings"""
    print_header("Updating Render Configuration")
    
    render_config = """services:
  - type: web
    name: vijayapardhu-portfolio
    env: python
    plan: starter
    region: oregon
    buildCommand: |
      pip install -r requirements.txt
      python manage.py collectstatic --noinput
      python manage.py migrate
    startCommand: gunicorn portfolio_template.wsgi:application --bind 0.0.0.0:$PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: DEBUG
        value: false
      - key: ALLOWED_HOSTS
        value: .onrender.com
      - key: DATABASE_URL
        fromDatabase:
          name: vijayapardhu-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: STATIC_URL
        value: /static/
      - key: MEDIA_URL
        value: /media/
      - key: EMAIL_HOST
        value: smtp.gmail.com
      - key: EMAIL_PORT
        value: 587
      - key: EMAIL_USE_TLS
        value: true
      - key: EMAIL_HOST_USER
        value: vijaypardhu17@gmail.com
      - key: EMAIL_HOST_PASSWORD
        sync: false

databases:
  - name: vijayapardhu-db
    env: postgres
    plan: basic
    region: oregon
    version: 15
"""
    
    with open('render.yaml', 'w') as f:
        f.write(render_config)
    
    print("✅ Updated render.yaml with current configuration")

def update_procfile():
    """Update Procfile for Render"""
    print_header("Updating Procfile")
    
    procfile_content = """web: gunicorn portfolio_template.wsgi:application --bind 0.0.0.0:$PORT
"""
    
    with open('Procfile', 'w') as f:
        f.write(procfile_content)
    
    print("✅ Updated Procfile")

def update_requirements():
    """Update requirements.txt for production"""
    print_header("Updating Requirements")
    
    requirements_content = """Django>=4.2.0,<5.0.0
gunicorn>=20.1.0,<22.0.0
whitenoise>=6.4.0,<7.0.0
python-decouple>=3.6,<4.0.0
django-crispy-forms>=2.0,<3.0.0
crispy-tailwind>=0.5.0,<1.0.0
Pillow>=9.5.0,<10.2.0
psycopg2-binary>=2.9.0,<3.0.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    
    print("✅ Updated requirements.txt for production")

def create_deployment_scripts():
    """Create deployment helper scripts"""
    print_header("Creating Deployment Scripts")
    
    # Create pre-deploy script
    pre_deploy_content = """#!/bin/bash
# Pre-deployment script for Render
echo "🚀 Starting pre-deployment tasks..."

# Install dependencies
pip install -r requirements.txt

# Run Django checks
python manage.py check --deploy

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

echo "✅ Pre-deployment tasks completed!"
"""
    
    with open('pre_deploy.sh', 'w') as f:
        f.write(pre_deploy_content)
    
    # Create post-deploy script
    post_deploy_content = """#!/bin/bash
# Post-deployment script for Render
echo "🎉 Post-deployment tasks starting..."

# Create admin user if it doesn't exist
python create_admin_auto.py

# Load portfolio data if database is empty
python load_portfolio_data.py

echo "✅ Post-deployment tasks completed!"
"""
    
    with open('post_deploy.sh', 'w') as f:
        f.write(post_deploy_content)
    
    # Make scripts executable (Unix-like systems)
    try:
        os.chmod('pre_deploy.sh', 0o755)
        os.chmod('post_deploy.sh', 0o755)
    except:
        pass  # Windows systems will ignore this
    
    print("✅ Created deployment helper scripts")

def create_render_dashboard_guide():
    """Create a guide for Render dashboard configuration"""
    print_header("Creating Render Dashboard Guide")
    
    guide_content = """# 🚀 Render Deployment Dashboard Guide

## 1. Create New Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repository: `portfolio_template`

## 2. Configure Service

- **Name**: `vijayapardhu-portfolio`
- **Environment**: `Python 3`
- **Region**: `Oregon` (or closest to your users)
- **Branch**: `main` (or your default branch)
- **Build Command**: 
  ```
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- **Start Command**: 
  ```
  gunicorn portfolio_template.wsgi:application --bind 0.0.0.0:$PORT
  ```

## 3. Environment Variables

Set these in the Render dashboard:

| Key | Value | Description |
|-----|-------|-------------|
| `DEBUG` | `false` | Production mode |
| `SECRET_KEY` | `generate` | Auto-generate secret key |
| `ALLOWED_HOSTS` | `.onrender.com` | Allow Render domains |
| `DATABASE_URL` | `from database` | Link to PostgreSQL |
| `EMAIL_HOST_USER` | `vijaypardhu17@gmail.com` | Your email |
| `EMAIL_HOST_PASSWORD` | `your-app-password` | Gmail app password |

## 4. Create PostgreSQL Database

1. Go to "New +" → "PostgreSQL"
2. Name: `vijayapardhu-db`
3. Region: Same as web service
4. Plan: `Basic` (free tier)
5. Link it to your web service

## 5. Deploy

1. Click "Create Web Service"
2. Wait for build to complete
3. Your portfolio will be live at: `https://vijayapardhu-portfolio.onrender.com`

## 6. Post-Deployment

1. Access admin: `https://vijayapardhu-portfolio.onrender.com/admin/`
2. Login with: `admin` / `admin123456`
3. Customize your portfolio content
4. Update email settings for contact form

## 🔧 Troubleshooting

- **Build fails**: Check requirements.txt and Python version
- **Database errors**: Ensure DATABASE_URL is set correctly
- **Static files not loading**: Check STATIC_URL and collectstatic
- **Email not working**: Verify SMTP settings and app passwords

## 📞 Support

If you encounter issues:
1. Check Render build logs
2. Verify environment variables
3. Test locally first
4. Check Django error logs in Render dashboard
"""
    
    with open('RENDER_DEPLOYMENT_GUIDE.md', 'w') as f:
        f.write(guide_content)
    
    print("✅ Created Render deployment guide")

def run_django_checks():
    """Run Django deployment checks"""
    print_header("Running Django Deployment Checks")
    
    # Check if migrations are needed
    print_step("1", "Checking Django deployment readiness")
    result = run_command("python manage.py check --deploy", "Django deployment check")
    
    if result:
        print("   ✅ Django deployment check passed")
    
    # Collect static files
    print_step("2", "Collecting static files")
    run_command("python manage.py collectstatic --noinput", "Static file collection")
    
    # Check database
    print_step("3", "Checking database")
    run_command("python manage.py showmigrations", "Migration status")

def create_git_instructions():
    """Create Git deployment instructions"""
    print_header("Creating Git Deployment Instructions")
    
    git_instructions = """# 🚀 Git Deployment Instructions

## 1. Initialize Git Repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit - Portfolio ready for Render deployment"
```

## 2. Add Remote Repository

```bash
git remote add origin https://github.com/Vijayapardhu/portfolio_template.git
```

## 3. Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## 4. Enable Auto-Deploy on Render

1. In Render dashboard, ensure "Auto-Deploy" is enabled
2. Every push to main branch will trigger automatic deployment
3. Monitor build logs for any issues

## 5. Update and Deploy

For future updates:
```bash
git add .
git commit -m "Update portfolio content"
git push origin main
```

## 🔄 Continuous Deployment

- Render will automatically detect changes
- Build and deploy on every push
- No manual intervention needed
- Monitor deployment status in dashboard
"""
    
    with open('GIT_DEPLOYMENT.md', 'w') as f:
        f.write(git_instructions)
    
    print("✅ Created Git deployment instructions")

def create_final_checklist():
    """Create final deployment checklist"""
    print_header("Creating Final Deployment Checklist")
    
    checklist = """# ✅ Final Deployment Checklist

## Before Deploying to Render

- [ ] All Django migrations applied locally
- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] Environment variables configured
- [ ] Database models tested locally
- [ ] Admin user created (`python setup_admin.py`)
- [ ] Portfolio data loaded (`python load_portfolio_data.py`)
- [ ] Contact form tested locally
- [ ] All pages load without errors

## Render Configuration

- [ ] Web service created and configured
- [ ] PostgreSQL database created and linked
- [ ] Environment variables set correctly
- [ ] Build command configured
- [ ] Start command configured
- [ ] Auto-deploy enabled

## Post-Deployment

- [ ] Website loads at Render URL
- [ ] Admin panel accessible
- [ ] Contact form sends emails
- [ ] All static files loading
- [ ] Database content visible
- [ ] Custom domain configured (optional)

## Security Checklist

- [ ] DEBUG set to false
- [ ] SECRET_KEY changed from default
- [ ] ALLOWED_HOSTS configured
- [ ] Admin password changed
- [ ] Email credentials secure
- [ ] HTTPS enabled (automatic on Render)

## Performance Checklist

- [ ] Static files served by CDN
- [ ] Database queries optimized
- [ ] Images compressed
- [ ] Caching enabled (if needed)
- [ ] Monitoring set up

## 🎯 Success Indicators

✅ Portfolio loads in under 3 seconds
✅ All pages render correctly
✅ Contact form sends emails
✅ Admin panel fully functional
✅ Mobile responsive design
✅ SEO meta tags working
✅ Social media links functional
"""
    
    with open('DEPLOYMENT_CHECKLIST.md', 'w') as f:
        f.write(checklist)
    
    print("✅ Created deployment checklist")

def main():
    """Main deployment function"""
    print_header("Django Portfolio Render Deployment")
    print("This script will prepare your Django portfolio for deployment on Render.")
    
    # Check prerequisites
    check_prerequisites()
    
    # Setup environment
    setup_environment()
    
    # Update configuration files
    update_render_config()
    update_procfile()
    update_requirements()
    
    # Create deployment scripts
    create_deployment_scripts()
    
    # Create documentation
    create_render_dashboard_guide()
    create_git_instructions()
    create_final_checklist()
    
    # Run Django checks
    run_django_checks()
    
    # Final summary
    print_header("🎉 Deployment Preparation Complete!")
    print("""
Your Django portfolio is now ready for Render deployment!

📁 Files Created/Updated:
   • .env (local development)
   • .env.production (production template)
   • render.yaml (Render configuration)
   • Procfile (Render process file)
   • requirements.txt (production dependencies)
   • pre_deploy.sh (deployment script)
   • post_deploy.sh (post-deployment script)
   • RENDER_DEPLOYMENT_GUIDE.md (step-by-step guide)
   • GIT_DEPLOYMENT.md (Git instructions)
   • DEPLOYMENT_CHECKLIST.md (deployment checklist)

🚀 Next Steps:
   1. Review RENDER_DEPLOYMENT_GUIDE.md
   2. Push your code to GitHub
   3. Create Render web service
   4. Configure environment variables
   5. Deploy and test

📚 Documentation:
   • RENDER_DEPLOYMENT_GUIDE.md - Complete deployment guide
   • GIT_DEPLOYMENT.md - Git and GitHub instructions
   • DEPLOYMENT_CHECKLIST.md - Final verification checklist

🌐 Your portfolio will be live at:
   https://vijayapardhu-portfolio.onrender.com

Need help? Check the documentation files or Render's support!
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Deployment preparation interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during deployment preparation: {e}")
        print("Please check the error and try again.")
