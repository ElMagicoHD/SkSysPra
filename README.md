# Programmierpraktikum: Skalierbare Systeme

Dynamic website developed with Bootstrap and Django frameworks which simulate simple ToDo-Tracker. Static ToDo, which was created before was used as skeleton for dynamic site. It has three functionalities: create new ToDo task, edit existing one and delete existing ToDo task. The data are stored persistently in a SQLite database.

## Installation guide for HA02:

Be sure your computer has python 3.6 or higher installed. Open your terminal in the "HA02/Website" folder.

## If you're on windows:
doubleclick on the **_startserver.cmd_** file!

## If you're on a UNIX based system:

type:
```
python ./HA02/Website/manage.py makemigrations

python ./HA02/Website/manage.py migrate

python ./HA02/Website/manage.py runserver
```
Then open the URL ```localhost:8000``` in your preferred browser!
