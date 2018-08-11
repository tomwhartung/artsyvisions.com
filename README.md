# artsyvisions.com

New version of artsyvisions.com .

- Using Django 2.1 and Materialize

## References

### Django Setup

- Notes from setting up seeourminds.com: https://github.com/tomwhartung/seeourminds.com/blob/master/README.md
- Setup tutorial: https://docs.djangoproject.com/en/2.1/intro/tutorial01/
- Install django: https://docs.djangoproject.com/en/2.1/topics/install/
- Version check: https://docs.djangoproject.com/en/2.1/faq/install/#faq-python-version-support

### Django Templates

- Template tutorial for 2.1: https://docs.djangoproject.com/en/2.1/intro/tutorial03/
- Template confusion fixer: https://tutorial.djangogirls.org/en/template_extending/

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

### 3. Use the `django-admin` Command to Run `startapp`

```
# Run in virtualenv window
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
cd Site/
django-admin startapp content
```

### 4. Edit Important Files to Get a Hello-world-type View Working

#### 4.1 The `settings.py` File

We do **not** keep the `settings.py` file in github, for obvious reasons.

Run these commands:

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
mkdir -p gitignored/Site/Site/RCS
touch gitignored/Site/Site/.this_dir_intentionally_left_empty
mv Site/Site/settings.py  gitignored/Site/Site/
cd Site/Site/
ln -s ../../gitignored/Site/Site/settings.py .
ga gitignored/Site/Site/.this_dir_intentionally_left_empty
cd -
ga gitignored/Site/Site/.this_dir_intentionally_left_empty
gc 'Adding empty hidden file gitignored/Site/Site/.this_dir_intentionally_left_empty ; see Step 5 in the README.md file.'
ga Site/Site/settings.py
gc 'The settings.py file is no longer a file, but a link to a file that we do not check in.'
cd gitignored/Site/Site/
ci -l settings.py   # Check in to RCS - "Installed version"
vi settings.py
```

Edit `gitignored/Site/Site/settings.py` , using the `settings.py` file from seeourminds.com as a guide, as follows:

- Change the secret key - yikes, it has already been checked in, oops!
  - https://www.miniwebtool.com/django-secret-key-generator/
    - Or similar
- Add code to set `DEBUG` based on values from the run environment
- Update `ALLOWED_HOSTS`
  - Add '.artsyvisions.com'
  - Add '0.0.0.0'
  - Add '127.0.0.1'
- Add `'content',` at the end of the list of `INSTALLED_APPS`
- Comment out the definition of `DATABASES` for now (and possibly forever!)
- Update the section at the end concerning static files
  - Add the comments
  - Add the declaration of STATIC_ROOT, changing `seeourminds` to `artsyvisions` as necessary

Run and check in browser, to ensure it still works:

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
cd Site/bin
./run.sh
```

Access in browser:

- http://127.0.0.1:8001/

When it works ok, check the new `settings.py` file into **RCS** - NOT github!!

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com   # `goa`
cd gitignored/Site/Site/
ci -l settings.py   # Check in to RCS - "First pass at updates needed.  For details, see Step 4.1 in the README.md file."
```

#### 4.2 The Other Files

Edit the other important files, using the versions in seeourminds.com as a guide, as follows:

- Edit `Site/content/views.py`, adding code from the tutorial:
  - https://docs.djangoproject.com/en/2.1/intro/tutorial01/#write-your-first-view
- Edit `Site/content/urls.py`
  - Add a route, so that visiting the site invokes `views.index` , the `index()` function in `views.py`
- Edit `Site/Site/urls.py` , so that we use the routes in `content/urls.py`
  - Add route for content:
    - `path('', include('content.urls')),`

Access in browser:

- http://127.0.0.1:8001/

Should see the "Hello world" message.

### 5. Add in the Materialize code

Here we deviate from the process used for seeourminds.com just a little bit, because we are using Materialize.
The steps are essentially the same, it's just we are getting the files from a different place, i.e.:

- `/var/www/always_learning/always_learning_google_products/material_design/04-prototypes/Site`

#### 5.1 Add Templates

Copy the materialize `index.html` into `content/templates/content` , rename to home.html , and edit as appropriate

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com/Site/content     ## `goavsc`
mkdir -p templates/content/
cd templates/content/
cp ...
mv index.html home.html
vi home.html
```

We will need to separate out the markup we want to use on all pages, e.g., head tag markup, navigation, and footer markup, into base.html .
Might as well do it now.

Using the templates in seeourminds.com as a guide....

#### 5.2 Add Static Files

Copy the supporting materialize css and js into the proper directories, `static/content/css` and `static/content/js`

```
cd /var/www/artsyvisions.com/htdocs/artsyvisions.com/Site/content     ## `goavsc`
mkdir -p Static/content/
cd Static/content/
cp ...
```

#### 5.3 Update the View

Update views.py to use the template instead of just returning the "hello world" text.

Using the templates in seeourminds.com as a guide....

These two references were quite helpful:

- https://docs.djangoproject.com/en/2.1/intro/tutorial03/
- https://tutorial.djangogirls.org/en/template_extending/

### 6. Apache Setup?

Not sure whether we will do that.
Might take it straight to the cloud.

