release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
release: python3 manage.py makemigrations allauth
release: python3 manage.py migrate allauth


web: gunicorn customuser.wsgi 