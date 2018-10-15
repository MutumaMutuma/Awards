# <img src="/static/pics/awards-academic-5.png" height="100px"> Awards
This is an app where users can review apps made by other devs

## Application
<img src="/static/pics/Screenshot from 2018-10-15 18-40-09.png">

## User stories

The user should be able to:

+ [x] View posted projects and their details.
+ [x] Post a project to be rated/reviewed
+ [x] Rate/ review other users' projects.
+ [x] Search for projects.
+ [x] View projects overall score
+ [x] View my profile page.

## Prerequisites
+ [x] Python3.6

## Installation
To install, follow the following instructions;

```bash
    $ git clone https://github.com/MutumaMutuma/Awards.git
    $ cd Awards
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver
```
## How to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

```bash
    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```
## Awards Demo

This is the live link to Awards [Click here](https://hawardsyamimi.herokuapp.com)

## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)
* [Bootstrap](https://www.getbootstrap.com/)

## License ([MIT License](https://github.com/MutumaMutuma/Awards/blob/master/LICENSE))
This project is licensed under the MIT Open Source license, (c) [Lewis Mutuma](https://github.com/MutumaMutuma)