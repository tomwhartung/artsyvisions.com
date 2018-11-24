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

### 6. Analyzing Versions in Use vs. Versions Available

**Goal: consistent versions on `bette` , `jane` , `barbara` , and `ava` .**

#### 6.1 New "v" for "Version" route on all sites

Each site now has a route "v" that displays the versions of python and of either django or flask the site is using.

- ArtsyVisions.com:
  - http://127.0.0.1:8001/v
- Groja.com:
  - http://127.0.0.1:5001/v
- SeeOurMinds.com:
  - http://127.0.0.1:8002/v

#### 6.2 Q: Update Version of python? A: NO

As of 2018-11-23, all hosts:

- Current version is python3.7
- Sites and rest of OS use Python 3.5.2 for python3
- python3.6 is installed but not used
  - OS may depend on using python3.5
  - All hosts are due for an OS upgrade
- python3.7 is available but I see no pressing need to install it
- Planning to start moving sites to the cloud - soon
- Just want to get the new work online ASAP

Therefore:

- **Continue using python3.5.2 for now**

#### 6.3 Q: Update Version of flask? A: WHEN MOVE TO CLOUD

As of 2018-11-23, all hosts:

- Current version is 0.12
- Groja.com is the only flask site
- No pressing need to upgrade

Therefore:

- **Continue using flask 0.12 for now**
- Upgrade when move site to cloud, which will probably be early next year

#### 6.4 Q: Update Version of django? A: YES

As of 2018-11-23, all hosts:

- Current global version is 1.10.2
- New version of ArtsyVisions.com **on bette only** is using 2.1
- Django version roadmap:
  - https://www.djangoproject.com/weblog/2015/jun/25/roadmap/
- A nice graphic version:
  - https://www.djangoproject.com/download/#supported-versions
- Choosing which version to use:
  - 1.11 LTS - Extended support through at least April 2020
  - 2.0 - Extended support through April 2019
- For consistency, I'd like both ArtsyVisions.com and SeeOurMinds.com to use 1.11

Therefore:

- Try 1.11 on ArtsyVisions.com **on bette only**
- Try 1.11 on SeeOurMinds.com **on bette only**
- If that works OK,
  - **Update all hosts to have django version 1.11 available globally**

##### 6.5 Upgrading Django - Details

- Current revision available: 1.11.17
  - https://docs.djangoproject.com/en/2.1/releases/1.11.17/
- Install using `pip`:

As tomh:
```
pip install Django==1.11.17   # Note: two ==
## Didn't work as hoped, but it suggested running this command, so I did:
pip install --upgrade pip
## Yikes, now pip is broken, trying fresh start
```

- Reference:
  - https://askubuntu.com/questions/561377/pip-wont-run-throws-errors-instead
  - **Note: commands used below are from what is currently the second answer**

```
sudo apt-get purge python-pip
sudo apt-get purge python3-pip
sudo apt install python-setuptools
sudo apt install python3-setuptools  # pip and pip3 are NOT available
sudo easy_install -U pip             # pip is now available to run
sudo easy_install3 -U pip            # pip3 is now available to run
sudo apt autoremove                  # apt install suggested running this
pip install Django==1.11.17          # "bash: /usr/bin/pip: No such file or directory"
pip3 install Django==1.11.17         # "No matching distribution found for Django==1.11.17"
pip3 install Django==1.11.16         # "Could not install packages due to an EnvironmentError: [Errno 13] Permission denied:
                                     #  '/usr/local/lib/python3.5/dist-packages/pytz-2018.7.dist-info'
                                     #  Consider using the `--user` option or check the permissions."
```
As root:
```
pip3 install Django==1.11.16         # "Successfully installed Django-1.11.16 pytz-2018.7"
```

Had to add '127.0.0.1' to ALLOWED_HOSTS for SeeOurMinds.com and now both it and ArtsyVisions.com seem to be working ok!

### 7. Apache Setup - on jane

1. Upgrade django (if encounter issues, see details above)
   - As root: `pip3 install Django==1.11.16`
   - Optional, as root: `pip install --upgrade pip`
   - NOTE: this broke pip earlier!
1. Pull code
1. Copy apache conf files from seeourminds.com to use on artsyvisions.com
1. Update new artsyvisions.com conf files
1. Restart apache, test the site, refine conf file, repeat as needed until it works



### 8. Deployment - on jane

### 8.1 Overview of Deployment Process

Deploy the new sites in this sequence:

- [ ] 1. artsyvisions.com
- [ ] 2. groja.com
- [ ] 3. seeourminds.com

Process overview:

1. Pull code
   [x] artsyvisions.com (done above)
   [ ] groja.com
   [ ] seeourminds.com
1. Run `bin/collectstatic.sh` for django sites
1. Update links if necessary
   - to settings.py file in gitignored
   - to dir referenced in apache conf
1. Restart apache
1. Test and fix as necessary




### 9. Deployment - on barbara

1. Upgrade django (if encounter issues, see details above)
   - As root: `pip3 install Django==1.11.16`
   - Optional, as root: `pip install --upgrade pip`
   - NOTE: this broke pip earlier!


### 10. Deployment - on ava




