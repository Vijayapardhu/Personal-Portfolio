"""
Fallback WSGI application for deployment platforms that expect app.py
This file redirects to the main Django WSGI application.
"""

from portfolio_template.wsgi import application

# For deployment platforms that expect 'app' variable
app = application