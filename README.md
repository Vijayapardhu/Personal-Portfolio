# Vijaya Pardhu - Portfolio Website

A modern, responsive portfolio website built with Django, featuring dynamic content management, CV generation, and beautiful UI design.

## 🚀 Features

- **Modern Design**: Clean, responsive design with TailwindCSS
- **Dynamic Content**: Admin panel to manage projects, skills, and achievements
- **CV Generation**: Automatic PDF CV generation with ReportLab
- **GitHub Integration**: Embedded GitHub statistics and project links
- **Mobile Responsive**: Optimized for all device sizes
- **Interactive Elements**: Smooth animations and hover effects
- **SEO Optimized**: Meta tags and structured content

## 🛠 Tech Stack

- **Backend**: Django 4.2.7
- **Frontend**: HTML5, CSS3, JavaScript, TailwindCSS
- **Database**: SQLite (development), PostgreSQL (production ready)
- **PDF Generation**: ReportLab
- **Icons**: Font Awesome
- **Animations**: AOS.js, Custom CSS animations

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow (for image handling)
- ReportLab (for PDF generation)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd portfolio_website
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Populate Initial Data

```bash
python manage.py populate_data
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see your portfolio!

## 📁 Project Structure

```
portfolio_website/
├── portfolio/                    # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── admin.py                # Admin panel configuration
│   ├── urls.py                 # URL routing
│   └── management/             # Custom management commands
│       └── commands/
│           └── populate_data.py
├── templates/                   # HTML templates
│   ├── base.html              # Base template
│   └── portfolio/             # App-specific templates
│       ├── home.html          # Home page
│       ├── about.html         # About page
│       ├── projects.html      # Projects page
│       └── contact.html       # Contact page
├── static/                     # Static files
│   ├── css/                   # Stylesheets
│   ├── js/                    # JavaScript files
│   └── images/                # Images and icons
├── media/                      # User-uploaded files
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

## 🎨 Customization

### Adding New Projects

1. Go to Django admin panel (`/admin/`)
2. Navigate to "Projects" section
3. Click "Add Project"
4. Fill in project details:
   - Title and description
   - Project type (Android, Web, AI, etc.)
   - GitHub URL
   - Technologies used
   - Featured status

### Managing Skills

1. In admin panel, go to "Skills" section
2. Add new skills with:
   - Name and category
   - Icon (emoji or text)
   - Proficiency percentage
   - Order for display

### Updating Achievements

1. Go to "Achievements" section in admin
2. Add new achievements with:
   - Title and description
   - Achievement type
   - Icon and date
   - Featured status

### Customizing CV

The CV is automatically generated from your portfolio data. To customize:

1. Update your information in the admin panel
2. Modify the CV template in `views.py` (download_cv function)
3. Customize styling in the ReportLab code

## 🌐 Deployment

### Production Settings

1. Update `settings.py`:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   ```

2. Set up environment variables:
   ```bash
   export SECRET_KEY='your-secret-key'
   export DATABASE_URL='your-database-url'
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

### Recommended Hosting

- **Render**: Easy Django deployment
- **Heroku**: Popular platform with good Django support
- **DigitalOcean**: VPS hosting with full control
- **AWS**: Scalable cloud hosting

## 📱 Mobile Optimization

The website is fully responsive and optimized for:
- Mobile phones (320px+)
- Tablets (768px+)
- Desktop (1024px+)
- Large screens (1280px+)

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration

For production, update database settings in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': '5432',
    }
}
```

## 🎯 Features in Detail

### Home Page
- Hero section with animated background
- Profile statistics (views, followers, stars)
- Featured projects showcase
- Skills display with proficiency bars
- Recent achievements
- Hobbies and interests
- GitHub statistics integration

### About Page
- Detailed education information
- Comprehensive skills breakdown
- Achievement timeline
- Career goals and aspirations

### Projects Page
- Grid layout of all projects
- Project filtering by type
- Technology tags
- GitHub and live demo links
- Project images and descriptions

### Contact Page
- Contact information display
- Contact form with validation
- Social media links
- Location and availability

### Admin Panel
- User-friendly interface
- Bulk editing capabilities
- Search and filtering
- Image upload support
- Data export options

## 🚀 Performance Optimization

- Lazy loading for images
- CSS and JavaScript minification
- Database query optimization
- Caching strategies
- CDN integration ready

## 🔒 Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure file uploads
- Admin panel security

## 📊 Analytics Integration

The website is ready for analytics integration:
- Google Analytics
- Google Search Console
- Social media tracking
- Performance monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Django community for the excellent framework
- TailwindCSS team for the utility-first CSS framework
- Font Awesome for the icon library
- ReportLab for PDF generation capabilities

## 📞 Support

If you have any questions or need help:

- Email: vijayapardhu17@gmail.com
- GitHub: [@Vijayapardhu](https://github.com/Vijayapardhu)
- Create an issue in this repository

## 🔄 Updates

### Version 1.0.0
- Initial release
- Complete portfolio functionality
- Admin panel
- CV generation
- Responsive design

### Planned Features
- Blog system
- Portfolio analytics
- Multi-language support
- Dark mode toggle
- Advanced search functionality

---

**Built with ❤️ by Vijaya Pardhu**

*Student | Android & Web Developer | Firebase Enthusiast*
