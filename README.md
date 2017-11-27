# Thirsty Cali

A fictional restaurant website where user can view menu offerings and make reservations.

## Prerequisites/Installing

To open Django project, please install django 1.11 and latest python 3.6 (or latest) turn on virtual environment on your terminal/bash

For Mac/Linux Users, please install python through [homebrew](https://brew.sh/)

For Windows Users, please install python [here](https://www.python.org/downloads/release/python-2713/)

```
#Create new directory called myEnvironments(or any name you want) and navigate there.
EX: $ cd ~/Documents/sser/python_stack/myEnvironments

#Mac/Linux
brew update #updates homebrew
brew install python #install python
pip install virtualenv 

#Inside the myEnvironments folder, create your first virtual environment
virtualenv djangoEnv(or name it whatever you want)

#On folder where your virtualEnvironment(s) are located at
source djangoEnv/bin/activate

#Windows
python -m virtualenv djangoEnv(or name whatever you want)

#Inside the myEnvironments folder, create your first virtual environment
virtualenv djangoEnv(or name it whatever you want)

#Choose of the following depending on your Windows command or git bash:
call djangoEnv/Scripts/activate #Windows command prompt
. djangoEnv/Scripts/activate #Windows 10 command prompt
source djangoEnv/Scripts/activate #Windows git bash


#All Users - after virtual environment is activated, install latest Django Version
pip install Django==1.11
```

## Opening the project (locally) to view the site.

Go to the project folder where it contains manage.py through your terminal/command and type:

```
python manage.py runserver
```

Once activated, you can browse to localhost:8000

## Built With

* [Python](https://www.python.org/) - Backend language used
* [Django](https://www.djangoproject.com/) - The web framework used
* [SQL](https://www.sqlite.org/) - Used to manage database

## Live Demo

* [Live Demo](http://54.146.235.215/) - Deployed through [AWS](https://aws.amazon.com/)

## Snapshot

### Mobile View
Mobile Navbar |Home/About |  Menu | Reservation
:---------:|:--------:|:---------:|:-----------
<img src="https://user-images.githubusercontent.com/25072657/33096827-2d870274-cebd-11e7-8a15-dab4651c9669.png" width="150"> | <img src="https://user-images.githubusercontent.com/25072657/33095223-ba503320-ceb7-11e7-948a-4207eef5608c.png" width="150"> |<img src="https://user-images.githubusercontent.com/25072657/33096863-4f75796a-cebd-11e7-96f6-a1f611b4458a.png" width="150">|<img src="https://user-images.githubusercontent.com/25072657/33096928-6fd8e570-cebd-11e7-9a12-0381cb309cfb.png" width="150">

### Desktop View
Home/About |  Menu | Reservation
:---------:|:--------:|:---------:
<img src="https://user-images.githubusercontent.com/25072657/33095037-0fdb3bf6-ceb7-11e7-80a3-4d7a9b0372ea.png" width="150"> | <img src="https://user-images.githubusercontent.com/25072657/33095728-87eb314e-ceb9-11e7-86dc-3b1caa25b59d.png" width="150"> | <img src="https://user-images.githubusercontent.com/25072657/33096390-adbe7b7c-cebb-11e7-9bbf-dbc58a86f948.png" width="150">

## Authors

* **Steve Kim** - [Suykim21](https://github.com/Suykim21)
