from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from portfolio.models import (
    ContactInfo, ProfileStats, Education, Skill, Hobby, 
    Project, Achievement, Experience, Certification
)

class Command(BaseCommand):
    help = 'Populate portfolio database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Starting to populate portfolio data...')
        
        # Contact Information
        contact_info, created = ContactInfo.objects.get_or_create(
            email='vijayapardhu17@gmail.com',
            defaults={
                'github_url': 'https://github.com/Vijayapardhu',
                'linkedin_url': 'https://linkedin.com/in/vijaya-pardhu',
                'phone': '+91 9876543210',
                'location': 'Surampalem, Andhra Pradesh, India'
            }
        )
        if created:
            self.stdout.write('✓ Contact information created')
        
        # Profile Statistics
        stats, created = ProfileStats.objects.get_or_create(
            profile_views=0,
            defaults={
                'github_followers': 25,
                'github_stars': 15,
                'projects_count': 8
            }
        )
        if created:
            self.stdout.write('✓ Profile statistics created')
        
        # Education
        education, created = Education.objects.get_or_create(
            degree='Diploma in Computer Engineering',
            institution='Aditya College of Engineering',
            defaults={
                'location': 'Surampalem, Andhra Pradesh',
                'start_year': 2023,
                'end_year': 2026,
                'current': True,
                'score': '76%',
                'description': 'Studying computer engineering with focus on software development, databases, and web technologies. Active in coding clubs and hackathons.'
            }
        )
        if created:
            self.stdout.write('✓ Education information created')
        
        # Skills
        skills_data = [
            # Programming Languages
            {'name': 'Java', 'category': 'programming', 'icon': 'fab fa-java', 'proficiency': 85, 'featured': True, 'order': 1},
            {'name': 'Kotlin', 'category': 'programming', 'icon': 'fab fa-android', 'proficiency': 80, 'featured': True, 'order': 2},
            {'name': 'Python', 'category': 'programming', 'icon': 'fab fa-python', 'proficiency': 75, 'featured': True, 'order': 3},
            {'name': 'PHP', 'category': 'programming', 'icon': 'fab fa-php', 'proficiency': 70, 'featured': False, 'order': 4},
            {'name': 'JavaScript', 'category': 'programming', 'icon': 'fab fa-js-square', 'proficiency': 75, 'featured': True, 'order': 5},
            {'name': 'HTML5', 'category': 'programming', 'icon': 'fab fa-html5', 'proficiency': 90, 'featured': False, 'order': 6},
            {'name': 'CSS3', 'category': 'programming', 'icon': 'fab fa-css3-alt', 'proficiency': 85, 'featured': False, 'order': 7},
            
            # Frameworks & Libraries
            {'name': 'Android SDK', 'category': 'frameworks', 'icon': 'fab fa-android', 'proficiency': 80, 'featured': True, 'order': 1},
            {'name': 'Django', 'category': 'frameworks', 'icon': 'fab fa-python', 'proficiency': 70, 'featured': True, 'order': 2},
            {'name': 'React Native', 'category': 'frameworks', 'icon': 'fab fa-react', 'proficiency': 65, 'featured': False, 'order': 3},
            {'name': 'Bootstrap', 'category': 'frameworks', 'icon': 'fab fa-bootstrap', 'proficiency': 80, 'featured': False, 'order': 4},
            {'name': 'Tailwind CSS', 'category': 'frameworks', 'icon': 'fas fa-palette', 'proficiency': 75, 'featured': False, 'order': 5},
            
            # Tools & IDEs
            {'name': 'Android Studio', 'category': 'tools', 'icon': 'fab fa-android', 'proficiency': 85, 'featured': True, 'order': 1},
            {'name': 'VS Code', 'category': 'tools', 'icon': 'fas fa-code', 'proficiency': 90, 'featured': True, 'order': 2},
            {'name': 'Git', 'category': 'tools', 'icon': 'fab fa-git-alt', 'proficiency': 80, 'featured': True, 'order': 3},
            {'name': 'GitHub', 'category': 'tools', 'icon': 'fab fa-github', 'proficiency': 85, 'featured': True, 'order': 4},
            {'name': 'Postman', 'category': 'tools', 'icon': 'fas fa-paper-plane', 'proficiency': 70, 'featured': False, 'order': 5},
            
            # Databases
            {'name': 'MySQL', 'category': 'databases', 'icon': 'fas fa-database', 'proficiency': 75, 'featured': True, 'order': 1},
            {'name': 'MongoDB', 'category': 'databases', 'icon': 'fas fa-leaf', 'proficiency': 65, 'featured': False, 'order': 2},
            {'name': 'SQLite', 'category': 'databases', 'icon': 'fas fa-database', 'proficiency': 80, 'featured': False, 'order': 3},
            
            # Cloud Services
            {'name': 'Firebase', 'category': 'cloud', 'icon': 'fas fa-fire', 'proficiency': 80, 'featured': True, 'order': 1},
            {'name': 'Google Cloud', 'category': 'cloud', 'icon': 'fab fa-google', 'proficiency': 60, 'featured': False, 'order': 2},
            {'name': 'AWS', 'category': 'cloud', 'icon': 'fab fa-aws', 'proficiency': 55, 'featured': False, 'order': 3},
            
            # Design Tools
            {'name': 'Figma', 'category': 'design', 'icon': 'fab fa-figma', 'proficiency': 70, 'featured': False, 'order': 1},
            {'name': 'Canva', 'category': 'design', 'icon': 'fas fa-palette', 'proficiency': 75, 'featured': False, 'order': 2},
            {'name': 'Adobe XD', 'category': 'design', 'icon': 'fas fa-paint-brush', 'proficiency': 60, 'featured': False, 'order': 3},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'✓ Skill "{skill.name}" created')
        
        # Hobbies
        hobbies_data = [
            {'name': 'Music & Podcasts', 'description': 'Love listening to music and tech podcasts while coding', 'icon': '🎵', 'color': 'purple', 'order': 1},
            {'name': 'UI Design', 'description': 'Creating beautiful and intuitive user interfaces', 'icon': '🎨', 'color': 'blue', 'order': 2},
            {'name': 'Experimenting with Tech', 'description': 'Always trying new technologies and frameworks', 'icon': '🔬', 'color': 'green', 'order': 3},
            {'name': 'Bible & Meditation', 'description': 'Finding peace and inspiration through faith', 'icon': '🙏', 'color': 'gold', 'order': 4},
            {'name': 'Problem Solving', 'description': 'Solving real-world problems through code', 'icon': '🧩', 'color': 'red', 'order': 5},
        ]
        
        for hobby_data in hobbies_data:
            hobby, created = Hobby.objects.get_or_create(
                name=hobby_data['name'],
                defaults=hobby_data
            )
            if created:
                self.stdout.write(f'✓ Hobby "{hobby.name}" created')
        
        # Projects
        projects_data = [
            {
                'title': 'HeySara - AI Assistant App',
                'short_description': 'An intelligent AI-powered personal assistant app for Android',
                'description': 'HeySara is a comprehensive AI assistant that helps users with daily tasks, reminders, and information queries. Features include voice recognition, natural language processing, and integration with various APIs.',
                'technologies': ['Kotlin', 'Android SDK', 'Firebase', 'OpenAI API', 'Google ML Kit'],
                'project_type': 'android',
                'difficulty_level': 'advanced',
                'github_url': 'https://github.com/Vijayapardhu/HeySara',
                'live_url': '',
                'icon': 'fas fa-robot',
                'featured': True,
                'completed_date': date(2024, 6, 15),
                'challenges_faced': 'Implementing real-time voice processing and integrating multiple AI APIs while maintaining app performance.',
                'lessons_learned': 'Learned about AI integration, voice processing, and optimizing Android apps for performance.',
                'impact': 'Helps users manage daily tasks efficiently with AI assistance.',
                'downloads_installs': 150,
                'stars': 8,
                'forks': 3
            },
            {
                'title': 'Church Management System',
                'short_description': 'Comprehensive church management solution for congregations',
                'description': 'A full-featured church management system that handles member registration, event management, donations tracking, and communication tools. Built with modern web technologies for easy access.',
                'technologies': ['Python', 'Django', 'MySQL', 'Bootstrap', 'JavaScript', 'Chart.js'],
                'project_type': 'web',
                'difficulty_level': 'intermediate',
                'github_url': 'https://github.com/Vijayapardhu/ChurchApp',
                'live_url': 'https://church-app-demo.herokuapp.com',
                'icon': 'fas fa-church',
                'featured': True,
                'completed_date': date(2024, 5, 20),
                'challenges_faced': 'Designing an intuitive interface for non-technical users and implementing secure user authentication.',
                'lessons_learned': 'User experience design, security best practices, and building scalable web applications.',
                'impact': 'Streamlines church operations and improves member engagement.',
                'downloads_installs': 0,
                'stars': 12,
                'forks': 5
            },
            {
                'title': 'Tourism Management System',
                'short_description': 'Complete tourism booking and management platform',
                'description': 'A comprehensive tourism management system that handles hotel bookings, tour packages, customer management, and payment processing. Features include a responsive design and admin dashboard.',
                'technologies': ['PHP', 'MySQL', 'HTML5', 'CSS3', 'JavaScript', 'jQuery', 'Bootstrap'],
                'project_type': 'web',
                'difficulty_level': 'intermediate',
                'github_url': 'https://github.com/Vijayapardhu/TourismSystem',
                'live_url': '',
                'icon': 'fas fa-plane',
                'featured': True,
                'completed_date': date(2024, 4, 10),
                'challenges_faced': 'Implementing complex booking logic and payment gateway integration.',
                'lessons_learned': 'Payment processing, booking system design, and database optimization.',
                'impact': 'Simplifies tourism business operations and improves customer experience.',
                'downloads_installs': 0,
                'stars': 6,
                'forks': 2
            },
            {
                'title': 'College Management System',
                'short_description': 'Student and faculty management system for educational institutions',
                'description': 'A comprehensive college management system that handles student records, faculty management, course scheduling, and grade management. Features role-based access control and reporting.',
                'technologies': ['Java', 'Swing', 'MySQL', 'JDBC', 'Apache POI'],
                'project_type': 'desktop',
                'difficulty_level': 'intermediate',
                'github_url': 'https://github.com/Vijayapardhu/CollegeManagement',
                'live_url': '',
                'icon': 'fas fa-graduation-cap',
                'featured': False,
                'completed_date': date(2024, 3, 25),
                'challenges_faced': 'Designing a user-friendly desktop interface and implementing complex data relationships.',
                'lessons_learned': 'Desktop application development, database design, and user interface design.',
                'impact': 'Improves administrative efficiency in educational institutions.',
                'downloads_installs': 0,
                'stars': 4,
                'forks': 1
            },
            {
                'title': 'SBTET Results Clone',
                'short_description': 'Student results checking system clone',
                'description': 'A clone of the SBTET results checking system that allows students to view their examination results by entering their roll number and other details.',
                'technologies': ['HTML', 'CSS', 'JavaScript', 'PHP', 'MySQL'],
                'project_type': 'web',
                'difficulty_level': 'beginner',
                'github_url': 'https://github.com/Vijayapardhu/SBTETResults',
                'live_url': '',
                'icon': 'fas fa-search',
                'featured': False,
                'completed_date': date(2024, 2, 15),
                'challenges_faced': 'Understanding the original system and implementing similar functionality.',
                'lessons_learned': 'Web development basics, form handling, and database queries.',
                'impact': 'Provides a familiar interface for students to check results.',
                'downloads_installs': 0,
                'stars': 3,
                'forks': 0
            },
            {
                'title': 'Weather App',
                'short_description': 'Real-time weather information Android app',
                'description': 'A weather application that provides current weather conditions, forecasts, and location-based weather alerts. Features include multiple city support and weather maps.',
                'technologies': ['Kotlin', 'Android SDK', 'OpenWeatherMap API', 'Google Maps API', 'Room Database'],
                'project_type': 'android',
                'difficulty_level': 'intermediate',
                'github_url': 'https://github.com/Vijayapardhu/WeatherApp',
                'live_url': '',
                'icon': 'fas fa-cloud-sun',
                'featured': False,
                'completed_date': date(2024, 1, 30),
                'challenges_faced': 'Integrating multiple APIs and handling offline data storage.',
                'lessons_learned': 'API integration, offline-first design, and location services.',
                'impact': 'Provides accurate weather information to users.',
                'downloads_installs': 75,
                'stars': 5,
                'forks': 1
            },
            {
                'title': 'Task Manager',
                'short_description': 'Personal task and project management tool',
                'description': 'A personal task manager that helps users organize their daily tasks, set priorities, and track progress. Features include categories, due dates, and progress visualization.',
                'technologies': ['Python', 'Tkinter', 'SQLite', 'Pillow'],
                'project_type': 'desktop',
                'difficulty_level': 'beginner',
                'github_url': 'https://github.com/Vijayapardhu/TaskManager',
                'live_url': '',
                'icon': 'fas fa-tasks',
                'featured': False,
                'completed_date': date(2023, 12, 20),
                'challenges_faced': 'Creating an intuitive user interface and implementing data persistence.',
                'lessons_learned': 'GUI development, data storage, and user experience design.',
                'impact': 'Helps users stay organized and productive.',
                'downloads_installs': 0,
                'stars': 2,
                'forks': 0
            },
            {
                'title': 'Portfolio Website',
                'short_description': 'Personal portfolio website built with Django',
                'description': 'A modern, responsive portfolio website showcasing projects, skills, and achievements. Features include dynamic content management, CV generation, and interactive elements.',
                'technologies': ['Python', 'Django', 'HTML5', 'CSS3', 'JavaScript', 'TailwindCSS', 'PostgreSQL'],
                'project_type': 'web',
                'difficulty_level': 'intermediate',
                'github_url': 'https://github.com/Vijayapardhu/Portfolio',
                'live_url': 'https://vijayapardhu.herokuapp.com',
                'icon': 'fas fa-user-tie',
                'featured': True,
                'completed_date': date(2024, 7, 1),
                'challenges_faced': 'Designing an attractive interface and implementing dynamic content management.',
                'lessons_learned': 'Full-stack development, responsive design, and deployment.',
                'impact': 'Showcases skills and projects professionally.',
                'downloads_installs': 0,
                'stars': 10,
                'forks': 4
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'✓ Project "{project.title}" created')
        
        # Achievements
        achievements_data = [
            {
                'title': 'Best Android Developer Award',
                'description': 'Received recognition for developing innovative Android applications at college tech fest',
                'achievement_type': 'award',
                'icon': '🏆',
                'date_achieved': date(2024, 5, 15),
                'featured': True
            },
            {
                'title': 'Google Developer Student Clubs Member',
                'description': 'Active member of GDSC, participating in workshops and hackathons',
                'achievement_type': 'certification',
                'icon': '👨‍💻',
                'date_achieved': date(2024, 3, 1),
                'featured': True
            },
            {
                'title': 'Hackathon Winner',
                'description': 'Won first place in college hackathon for developing a social impact project',
                'achievement_type': 'award',
                'icon': '🥇',
                'date_achieved': date(2024, 2, 20),
                'featured': True
            },
            {
                'title': 'Firebase Certification',
                'description': 'Completed Google Firebase Fundamentals certification',
                'achievement_type': 'certification',
                'icon': '🔥',
                'date_achieved': date(2024, 1, 10),
                'featured': False
            },
            {
                'title': 'Open Source Contributor',
                'description': 'Made contributions to various open-source projects on GitHub',
                'achievement_type': 'project',
                'icon': '🌟',
                'date_achieved': date(2023, 12, 15),
                'featured': False
            }
        ]
        
        for achievement_data in achievements_data:
            achievement, created = Achievement.objects.get_or_create(
                title=achievement_data['title'],
                defaults=achievement_data
            )
            if created:
                self.stdout.write(f'✓ Achievement "{achievement.title}" created')
        
        # Experience
        experience_data = [
            {
                'title': 'Freelance Android Developer',
                'company': 'Self-Employed',
                'experience_type': 'freelance',
                'location': 'Remote',
                'start_date': date(2023, 9, 1),
                'end_date': None,
                'current': True,
                'description': 'Developing custom Android applications for clients, including church management apps and business solutions. Working with various technologies and delivering high-quality products.',
                'technologies_used': ['Kotlin', 'Java', 'Android SDK', 'Firebase', 'MySQL'],
                'achievements': 'Delivered 5+ successful projects, maintained 4.8+ star rating from clients'
            },
            {
                'title': 'College Tech Club Lead',
                'company': 'Aditya College of Engineering',
                'experience_type': 'volunteer',
                'location': 'Surampalem, AP',
                'start_date': date(2023, 8, 1),
                'end_date': None,
                'current': True,
                'description': 'Leading the college technology club, organizing workshops, hackathons, and coding competitions. Mentoring junior students in programming and development.',
                'technologies_used': ['Python', 'Java', 'Web Technologies', 'Git'],
                'achievements': 'Organized 3 successful hackathons, mentored 20+ students'
            },
            {
                'title': 'Web Development Intern',
                'company': 'Local Web Agency',
                'experience_type': 'internship',
                'location': 'Visakhapatnam, AP',
                'start_date': date(2023, 6, 1),
                'end_date': date(2023, 8, 31),
                'current': False,
                'description': 'Worked on various web development projects using modern technologies. Gained experience in frontend and backend development, database design, and deployment.',
                'technologies_used': ['HTML5', 'CSS3', 'JavaScript', 'PHP', 'MySQL', 'Bootstrap'],
                'achievements': 'Completed 3 client projects, learned deployment and hosting'
            }
        ]
        
        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                title=exp_data['title'],
                company=exp_data['company'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'✓ Experience "{experience.title}" created')
        
        # Certifications
        certifications_data = [
            {
                'name': 'Google Firebase Fundamentals',
                'issuing_organization': 'Google',
                'credential_id': 'FIREBASE-2024-001',
                'issue_date': date(2024, 1, 10),
                'expiry_date': None,
                'credential_url': 'https://firebase.google.com/certification',
                'description': 'Comprehensive understanding of Firebase services including Authentication, Firestore, Cloud Functions, and Hosting.',
                'featured': True
            },
            {
                'name': 'Android Development Fundamentals',
                'issuing_organization': 'Google Developers',
                'credential_id': 'ANDROID-2023-001',
                'issue_date': date(2023, 11, 15),
                'expiry_date': None,
                'credential_url': 'https://developers.google.com/android',
                'description': 'Core Android development concepts including UI design, data storage, and app lifecycle management.',
                'featured': True
            },
            {
                'name': 'Python Programming',
                'issuing_organization': 'Coursera',
                'credential_id': 'PYTHON-2023-001',
                'issue_date': date(2023, 9, 20),
                'expiry_date': None,
                'credential_url': 'https://coursera.org',
                'description': 'Comprehensive Python programming course covering fundamentals, data structures, and web development.',
                'featured': False
            },
            {
                'name': 'Web Development Bootcamp',
                'issuing_organization': 'Udemy',
                'credential_id': 'WEB-2023-001',
                'issue_date': date(2023, 7, 10),
                'expiry_date': None,
                'credential_url': 'https://udemy.com',
                'description': 'Full-stack web development course covering HTML, CSS, JavaScript, and backend technologies.',
                'featured': False
            }
        ]
        
        for cert_data in certifications_data:
            certification, created = Certification.objects.get_or_create(
                name=cert_data['name'],
                issuing_organization=cert_data['issuing_organization'],
                defaults=cert_data
            )
            if created:
                self.stdout.write(f'✓ Certification "{certification.name}" created')
        
        self.stdout.write(self.style.SUCCESS('✓ Portfolio data population completed successfully!'))
        self.stdout.write('You can now access the admin panel to customize the content.')
