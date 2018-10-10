"""
WSGI config for Reports project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""


import os, sys



sys.path.insert(0,'/home/santosh/Documents/project/Reports')

# add the virtualenv site-packages path to the sys.path
sys.path.insert(0,'/home/santosh/Documents/project/project/lib/python3.5/site-packages')
sys.path.insert(0,'/home/santosh/Documents/project/project')
 




from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Reports.settings")

application = get_wsgi_application()