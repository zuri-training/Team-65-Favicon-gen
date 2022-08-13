# Backend

##  Tech Stack
  - Django
  - Postgres
  - Cloudinary

##  Settings.py

### Static Files
We used [django.contrib.staticfiles](https://docs.djangoproject.com/en/4.0/howto/static-files/) to manage our static files by including the below code in our settings file.


AUTHentication: We used django.allauth, as it is an ‘integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication’[1](https://django-allauth.readthedocs.io/en/latest/). Unlike other available authentication methods, it offers a fully integrated authentication app that allows for both local and social authentication.

Accounts App: Uses the django ‘AbstractUse’ model. This enabled us enjoy the ease of using the defaults of the django user model, while being able to extend it for our personal use case. Official documentation of the model is [here](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

Core App:Using django’s ‘model’ module to create two models and subsequently two tables in the database. We created the image model and the favicon_zip model
The image model: It’s field contain user_id, image_name, image_url, and image_upload_date.
The favicon_zip model: It’s field contain user_id, image_id, favicon_name, favicon_zip_url, favicon_creation_date.
