@echo off 

if "%1"=="" goto noargs
if "%1"==run goto djrun
if "%1"==migrate goto djmigrate
if "%1"==push goto djpush

:djpush
powershell write-host -fore Green DJ: Pushing to github...
git add .
git commit -m "dj push"
git push origin master
powershell write-host -fore Green DJ: Pushing to heroku...
git push heroku master
heroku ps:scale web=1
heroku open

:djrun
powershell write-host -fore Green DJ: Running server...
start chrome http://127.0.0.1:8000/
python manage.py runserver
goto commonexit

:djmigrate
powershell write-host -fore Green DJ: Migrating...
python manage.py migrate
python manage.py makemigrations
goto commonexit

:noargs
powershell write-host -fore Red DJ:No arguments were given

goto commonexit

:commonexit
exit /b