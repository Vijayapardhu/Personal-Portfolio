"""
WSGI config for portfolio_template project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_template.settings')

application = get_wsgi_application()
