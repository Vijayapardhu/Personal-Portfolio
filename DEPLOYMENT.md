# 🚀 Deploy Django Portfolio Template to Render

This guide will walk you through deploying your Django portfolio template to Render, a modern cloud platform that makes deployment simple and automatic.

## 📋 Prerequisites

- ✅ Django project is working locally
- ✅ Git repository is set up and committed
- ✅ GitHub/GitLab account
- ✅ Render account (free tier available)

## 🔧 Step 1: Prepare Your Project

### Run the deployment preparation script:
```bash
python deploy.py
```

This script will:
- Create a `.env` file for local development
- Run Django deployment checks
- Collect static files
- Verify your project is ready for production

## 🌐 Step 2: Push to GitHub/GitLab

### If you haven't already, push your code:
```bash
git add .
git commit -m "Ready for deployment on Render"
git push origin master
```

## 🚀 Step 3: Deploy on Render

### 1. Sign up/Login to Render
- Go to [render.com](https://render.com)
- Sign up with your GitHub/GitLab account

### 2. Create New Web Service
- Click "New +" → "Web Service"
- Connect your GitHub/GitLab repository
- Select the `portfolio-template` repository

### 3. Configure the Service
Render will automatically detect the `render.yaml` configuration:

**Service Details:**
- **Name:** `portfolio-template` (or your preferred name)
- **Environment:** `Python 3`
- **Region:** Choose closest to your users
- **Branch:** `master`
- **Build Command:** Automatically set from `render.yaml`
- **Start Command:** Automatically set from `render.yaml`

**Environment Variables:**
The following will be automatically set:
- `PYTHON_VERSION`: 3.9.16
- `SECRET_KEY`: Auto-generated
- `DEBUG`: false
- `ALLOWED_HOSTS`: portfolio-template.onrender.com

**Manual Environment Variables to Set:**
- `EMAIL_HOST_USER`: Your Gmail address
- `EMAIL_HOST_PASSWORD`: Your Gmail app password

### 4. Deploy
- Click "Create Web Service"
- Render will automatically build and deploy your app
- First deployment takes 5-10 minutes

## 🔐 Step 4: Configure Email (Optional)

### For Gmail:
1. Enable 2-factor authentication
2. Generate an App Password
3. Set in Render environment variables:
   - `EMAIL_HOST_USER`: your-email@gmail.com
   - `EMAIL_HOST_PASSWORD`: your-app-password

## 📱 Step 5: Access Your Portfolio

Once deployed, your portfolio will be available at:
```
https://portfolio-template.onrender.com
```

## 🛠️ Step 6: Admin Access

### Create a superuser for admin access:
```bash
# Locally
python manage.py createsuperuser

# Or via Render shell
# Go to Render dashboard → Your service → Shell
# Then run: python manage.py createsuperuser
```

## 🔄 Automatic Deployments

- **Auto-deploy:** Enabled by default
- **Deploy on push:** Every push to master triggers a new deployment
- **Preview deployments:** Available for pull requests

## 📊 Monitoring & Logs

- **Logs:** Available in Render dashboard
- **Metrics:** CPU, memory, and request monitoring
- **Health checks:** Automatic health monitoring

## 🚨 Troubleshooting

### Common Issues:

1. **Build fails:**
   - Check `requirements.txt` for compatibility
   - Verify Python version in `render.yaml`

2. **Static files not loading:**
   - Ensure `whitenoise` is in `MIDDLEWARE`
   - Check `STATIC_ROOT` and `STATICFILES_STORAGE`

3. **Database errors:**
   - Verify migrations are included in `render.yaml`
   - Check database configuration

4. **Email not working:**
   - Verify Gmail app password
   - Check environment variables in Render

### Debug Mode (Temporary):
```bash
# In Render environment variables, set:
DEBUG=true
```

## 🎯 Production Checklist

- [ ] `DEBUG = False` in production
- [ ] `SECRET_KEY` is properly set
- [ ] `ALLOWED_HOSTS` includes your domain
- [ ] Static files are collected
- [ ] Database migrations are applied
- [ ] Email configuration is working
- [ ] Admin user is created
- [ ] SSL certificate is active (automatic on Render)

## 🔗 Useful Links

- [Render Documentation](https://render.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [WhiteNoise Documentation](https://whitenoise.evans.io/)

## 🎉 Success!

Your Django portfolio is now live on the internet! Share your portfolio URL with potential employers, clients, and the world.

---

**Need Help?** Check the Render logs or Django documentation for specific error messages.
