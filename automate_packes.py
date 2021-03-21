import sys
import subprocess


# implement pipenv as subprocess
subprocess.check_call([sys.executable, '-m', 'pipenv', 'install', 'django', 'pillow', 'bcrypt', 'pylint-django', 'django-filter'])
subprocess.check_output([sys.executable, 'm', 'pipenv', 'shell'])
