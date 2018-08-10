# artsyvisions.com

New version of artsyvisions.com .

- Using Django 2.1 and Materialize

## References

### Django Setup

- Notes from setting up seeourminds.com: https://github.com/tomwhartung/seeourminds.com/blob/master/README.md
- Setup tutorial: https://docs.djangoproject.com/en/2.1/intro/tutorial01/
- Install django: https://docs.djangoproject.com/en/2.1/topics/install/
- Version check: https://docs.djangoproject.com/en/2.1/faq/install/#faq-python-version-support

### Front End: Using Materialize

- https://github.com/tomwhartung/always_learning_google_products/blob/master/material_design/README.md

## Process

Following process used for SeeOurMinds.com , updated to use version 2.1 of django.

### 1. Setup virtual environment, git clone django, and install it in the virtual env

As mentioned, reviewing the process used for seeourminds.com , and just noting the commands run:

```
which pip3        ## already installed on bette
which virtualenv  ## already installed on bette
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
mkdir virtualenvs
virtualenv --python=`which python3` virtualenvs/artsyvisions_env
mkdir bin
cat > bin/artsyvisions_env.sh
. /var/www/artsyvisions.com/htdocs/artsyvisions.com/virtualenvs/artsyvisions_env/bin/activate
[Ctrl-D]
chmod 755 bin/artsyvisions_env.sh
. bin/artsyvisions_env.sh
which python         ## /var/www/artsyvisions.com/htdocs/artsyvisions.com/virtualenvs/artsyvisions_env/bin/python
python               ## Python 3.5.2 - OK to use with django 2.1
pip install Django   ## Successfully installed Django-2.1 pytz-2018.5
```

### 2. Use the django-admin command to run startproject

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
. bin/artsyvisions_env.sh
django-admin startproject Site
cd Site
python manage.py runserver 0.0.0.0:8001     ## Ignore warnings about migrations
```

Note: seeourminds.com uses port 8000.

Access in browser:

- http://127.0.0.1:8001/

Should see page with "The install worked successfully! Congratulations!"



