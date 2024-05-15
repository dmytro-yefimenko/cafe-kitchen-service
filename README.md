# Cafe Kitchen Service
> This is a demo project

A cafe management system aimed at improving communication and rules between cooks in the kitchen.

## Check it out:
[Cafe Kitchen Service deployed to Render](https://cafe-kitchen-service.onrender.com/)

## Installation

Python3 must be installed

```shell
git clone https://github.com/dmytro-yefimenko/cafe-kitchen-service.git
cd cafe-kitchen-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver  # runs Django server
```

#### Be sure to create an .env file and fill it out as specified in .env.example file


## Features

* Authentication functionality for Chef/User
* Creating and updating dishes and dish types. Setting the price and description for them
* Managing chefs and keeping track of who can cook what dish


## Admin credentials
> username: admin
>
> password: 1!Password1!