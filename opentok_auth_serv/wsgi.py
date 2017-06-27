"""
WSGI config for opentok_auth_serv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import site
import sys
from django.core.wsgi import get_wsgi_application


site.addsitedir('/home/sushinski/virtualenvs/opentok_serv/opentok_serv/lib/python3.5/site-packages')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

if os.path.exists("/home/sushinski/virtualenvs/opentok_serv/opentok_serv/bin/"):
    activate_env = os.path.expanduser("/home/sushinski/virtualenvs/opentok_serv/opentok_serv/bin/activate_this.py")
    exec(open(activate_env).read())
else:
    w_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../opentok_serv/Scripts"))
    if os.path.exists(w_path):
        activate_env = os.path.join(w_path, "activate_this.py")
        exec(open(activate_env).read())

os.environ["DJANGO_SETTINGS_MODULE"] = "opentok_auth_serv.settings"

application = get_wsgi_application()

