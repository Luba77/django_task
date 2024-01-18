# Django Project

This project is a web application based on Django Rest Framework.

## Installation

```bash
git clone https://github.com/Luba77/django_task.git

# Install and activate virtual env depends on your system
#### Example (windows system):
pip install virtualenv
virtualenv venv
venv/Scripts/activate

# Next steps
cd django_task
pip install -r requirements.txt

### Put secret key
in settings.py put SECRET KEY from file 'key.txt'

python manage.py migrate
```

## Running
```bash
python manage.py runserver
```

The server will be available at http://127.0.0.1:8000/.

## URL Patterns

### /teams/: Displays a list of teams and allows creating new teams.

### /teams/<int:pk>/: Displays details of a specific team.

### /person/: Shows a list of persons and allows creating new entries.

### /person/<int:pk>/: Displays details of a specific person.



