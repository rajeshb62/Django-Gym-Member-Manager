"""
WSGI config for Gymnasium project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
#from notifications.config import get_notification_count, run_notifier


from django.core.wsgi import get_wsgi_application
#run_notifier()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Gymnasium.settings")

application = get_wsgi_application()
