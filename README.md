# Development Notes

    Issues with migrating over to wsl ubuntu for workflow
    restarted venv
    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt
    python -m pip install --upgrade pip

## Root Directory

    C:\Users\Administrator\Documents\GitHub\django-portfolio

# Project Structure

django-portfolio

```bash
use tree -I 'env|__pycache__' to update

├── Procfile
├── Procfile.windows
├── README.md
├── app.json
├── db.sqlite3
├── home
│   ├── __init__.py
│   ├── admin.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_remove_job_github_url_remove_job_heroku_url_and_more.py
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── jobs.html
│   ├── tests.py
│   └── views.py
├── manage.py
├── myproject
│   ├── __init__.py
│   ├── settings.py
│   ├── static
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── runtime.txt
└── staticfiles

```


# Push to Github
project located at https://github.com/anna-smith97/django-portfolio

    git add .

    git commit -m "commitment message"

    git push origin master


# Heroku
Dashboard https://dashboard.heroku.com/apps/annasmith

Production site https://annasmith.herokuapp.com/

### Updates:
    
    git push heroku master
    heroku ps:scale web=1
    heroku open

# Run development server
    python manage.py runserver

Located at http://127.0.0.1:8000/
    


# Migrations

    python manage.py migrate
    python manage.py makemigrations

# Activate virtual environment
    
    .env\Scripts\activate