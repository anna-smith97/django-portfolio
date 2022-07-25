@echo off 
echo 
set input1=%1
echo %input1%

if %input1%=="" goto noargs 
if %input1%==run goto djrun
if %input1%==migrate goto djmigrate 
if %input1%==push goto djpush


:noargs
powershell write-host -fore Red DJ: No arguments were given
powershell write-host -fore Red DJ: Try run migrate or push
goto commonexit

:djrun
powershell write-host -fore Green DJ: Running server...
start chrome http://127.0.0.1:8000/
python manage.py runserver
goto commonexit

:djmigrate
powershell write-host -fore Green DJ: Migrating...
python manage.py makemigrations
python manage.py migrate

goto commonexit

:djpush
powershell write-host -fore Green DJ: Pushing to github...
git add .
git commit -m "dj push"
git push origin master
powershell write-host -fore Green DJ: Pushing to heroku...
git push heroku master
heroku ps:scale web=1
heroku open
goto commonexit


:commonexit
exit /b