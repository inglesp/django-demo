# Django Demo

This repository tests that you've got Django installed correctly.  The
repository contains a simple web app that lists people's names and their dates
of birth.

You'll check out the app's code, install Django into a virtualenv, run the test
suite, and then verify that the app's pages are accessible in a browser.


## Instructions

If at any stage you see something that doesn't match the expected output, get
in touch!

* Clone this repository, and from the command line, change to the directory
  containing this README.
* Create and activate a [virtualenv](https://virtualenv.pypa.io/en/stable/).
* Run `pip install -r requirements.txt` to install Django.  You should see
  output including:

    Successfully installed Django-1.9.7

* Run `python manage.py test`.  You should see output matching:

    Creating test database for alias 'default'...
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.033s

    OK
    Destroying test database for alias 'default'...

* Run `python manage.py migrate`.  You should see output matching:

    Operations to perform:
      Apply all migrations: auth, admin, sessions, demo, contenttypes
    Running migrations:
      Rendering model states... DONE
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying demo.0001_initial... OK
      Applying sessions.0001_initial... OK

* Run `python manage.py createsuperuser` and answer the questions as prompted.
* Run `python manage.py runserver`.  You should see output matching:

    Performing system checks...

    System check identified no issues (0 silenced).
    July 07, 2016 - 11:13:11
    Django version 1.9.7, using settings 'demo.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

* In a browser, navigate to http://localhost:8000/.  You should see the text
  "Found no records".
* Then navigate to http://localhost:8000/admin/, and log in using the
  credentials you supplied when you ran the `createsuperuser` command.
* Click "People", and then "ADD PERSON", and fill out the form and click "SAVE"
  to add a person to the database.
* Now navigate to http://localhost:8000/ again.  You should now see "Found
  records for 1 person"
