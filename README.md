# 🚀 Django Portfolio Website Template

A fully customizable, production-ready Django portfolio website template with modern design, animations, and dynamic content management.

## ✨ Features

- **🎨 Modern Design**: Built with TailwindCSS for beautiful, responsive UI
- **✨ Animations**: AOS (Animate On Scroll) library for smooth animations
- **🌙 Dark Mode**: Built-in dark/light mode toggle
- **📱 Responsive**: Mobile-first design that works on all devices
- **🔧 Dynamic Content**: All content managed through Django Admin
- **📧 Contact Form**: Functional contact form with email backend
- **🚀 Deployment Ready**: Includes Render deployment configuration

## 🏗️ Project Structure

```
portfolio_template/
├── portfolio_template/          # Main project settings
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── main/                       # Main app
│   ├── __init__.py
│   ├── admin.py                # Admin panel configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Contact form
│   ├── models.py               # Database models
│   ├── urls.py                 # App URL patterns
│   └── views.py                # View functions
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   └── main/                   # Page templates
│       ├── home.html           # Home page
│       ├── about.html          # About page
│       ├── projects.html       # Projects page
│       ├── project_detail.html # Individual project page
│       ├── skills.html         # Skills page
│       ├── achievements.html   # Achievements page
│       └── contact.html        # Contact page
├── static/                     # Static files (CSS, JS, images)
├── media/                      # User-uploaded files
├── requirements.txt            # Python dependencies
├── Procfile                   # Render deployment
├── render.yaml                # Render configuration
├── env.example                # Environment variables example
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Git

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd portfolio_template
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file and configure it:

```bash
cp env.example .env
```

Edit `.env` with your settings:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your portfolio!

## 🎨 Customization Guide

### 1. Profile Information

1. Go to Django Admin (`/admin/`)
2. Navigate to "Profile" section
3. Add your personal information:
   - Name, tagline, about text
   - Profile picture
   - Contact details
   - Resume file

### 2. Skills

1. Go to "Skills" section in admin
2. Add your technical skills:
   - Name and category
   - Proficiency level (0-100%)
   - Icon URL (from skillicons.dev or FontAwesome)
   - Display order

### 3. Projects

1. Go to "Projects" section in admin
2. Add your portfolio projects:
   - Title and descriptions
   - Project images
   - GitHub and live demo links
   - Tech stack (select from skills)
   - Mark as featured if desired

### 4. Achievements

1. Go to "Achievements" section in admin
2. Add your accomplishments:
   - Title and description
   - Year achieved
   - Custom icon (emoji or text)

### 5. Social Links

1. Go to "Social Links" section in admin
2. Add your social media profiles:
   - Platform selection
   - Profile URLs
   - FontAwesome icon classes

### 6. Site Settings

1. Go to "Site Settings" section in admin
2. Customize:
   - Site name and hero text
   - Theme colors
   - Enable/disable features

## 🎯 Content Recommendations

### Profile Section
- **Name**: Your full name
- **Tagline**: Professional one-liner (e.g., "Full-Stack Developer | Problem Solver | Tech Enthusiast")
- **About Text**: 2-3 paragraphs about your background, passion, and goals
- **Profile Picture**: Professional headshot (recommended: 400x400px)
- **Resume**: PDF format for easy downloading

### Skills Section
- **Programming Languages**: Python, JavaScript, Java, etc.
- **Frameworks**: Django, React, Android, etc.
- **Databases**: PostgreSQL, MySQL, MongoDB, etc.
- **Tools**: Git, Docker, AWS, etc.

### Projects Section
- **Featured Projects**: Your best 3-4 projects
- **Project Images**: High-quality screenshots
- **Descriptions**: Clear explanation of what you built and why
- **Tech Stack**: Technologies used in each project
- **Links**: GitHub code and live demos

### Achievements Section
- **Certifications**: Professional certifications
- **Awards**: Hackathon wins, competitions
- **Publications**: Blog posts, articles
- **Contributions**: Open source contributions

## 🚀 Deployment to Render

### 1. Push to GitHub

```bash
git add .
git commit -m "Initial portfolio setup"
git push origin main
```

### 2. Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `portfolio-template`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn portfolio_template.wsgi:application`
5. Set environment variables (copy from `render.yaml`)
6. Click "Create Web Service"

### 3. Configure Domain

Your portfolio will be available at: `https://portfolio-template.onrender.com`

## 🔧 Configuration Options

### Theme Colors

Customize colors in Django Admin → Site Settings:
- **Primary Color**: Main brand color (default: #3B82F6)
- **Secondary Color**: Secondary brand color (default: #1F2937)
- **Accent Color**: Highlight color (default: #10B981)

### Features

Toggle features in Django Admin → Site Settings:
- **Dark Mode**: Enable/disable dark mode toggle
- **Animations**: Enable/disable AOS animations

### Email Configuration

Configure contact form email in `.env`:
- **Gmail**: Use App Password (not regular password)
- **Other Providers**: Update SMTP settings accordingly

## 📱 Mobile Optimization

The template is fully responsive with:
- Mobile-first design approach
- Touch-friendly navigation
- Optimized images and layouts
- Fast loading on mobile devices

## 🔒 Security Features

- CSRF protection on all forms
- Secure file uploads
- Environment variable configuration
- Production-ready settings

## 🚀 Performance Optimization

- WhiteNoise for static file serving
- Optimized images and assets
- Efficient database queries
- CDN-ready static files

## 🐛 Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_ROOT` in settings

2. **Media files not working**
   - Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured
   - Check file permissions

3. **Email not sending**
   - Verify SMTP settings in `.env`
   - Check email provider credentials
   - Use App Password for Gmail

4. **Database errors**
   - Run migrations: `python manage.py migrate`
   - Check database configuration

### Getting Help

- Check Django documentation
- Review error logs in console
- Verify environment variables
- Test with minimal data first

## 🤝 Contributing

This is a template project, but if you find bugs or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - Web framework
- [TailwindCSS](https://tailwindcss.com/) - CSS framework
- [AOS](https://michalsnik.github.io/aos/) - Animation library
- [FontAwesome](https://fontawesome.com/) - Icons
- [Render](https://render.com/) - Hosting platform

## 📞 Support

If you need help setting up or customizing your portfolio:

1. Check this README first
2. Review Django documentation
3. Check the admin panel for configuration options
4. Test with sample data before adding your content

---

**Happy coding! 🚀**

Your portfolio website is now ready to showcase your skills and projects to the world!
