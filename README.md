# Team-65-Favicon-gen
A web app that generates favicon of different sizes for different use cases for users

A platform that allows users to generate favicons – both icon and related codes to embed.
Platform in the sense that it can be a web application (web app) or a website.
Users or companies can visit this platform to generate their favicons


## Tech Stark

* **Backend**
  * Django(framework)
  * Postgres(DBMS)
  * Cloudinary(Image storage)
* **Frontend**
  * HTML
  * CSS
  * javascript
  
  
##  How Iconator Works

*Iconator takes an image, either jpeg, png ......., and creates a folder containing png and ico favicons as well as html code to be used with your website*

To view the [Iconator](www.iconator.com) website, use this [link](www.iconator.com)

The following is required from every user before you can access the features of __Iconator__
1.  Username
1.  Email
1.  Password
1.  First name
1.  Last name
1.  Country

Click [Signup](www.iconator.com/signup) to signup on the platform and [Signin](www.iconator.com/signin) to login if you already have an account

## Repository Tree Structure

```
├── README.md
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── engine.py
│   ├── migrations
│   ├── models.py
│   ├── site.webmanifest
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── favicon_gen
│   ├── __init__.py
│   ├── accounts
│   ├── asgi.py
│   ├── core
│   ├── favicon_gen
│   ├── frontend
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── local
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── manage.py
├── my_file.py
├── requirements.txt
├── static
│   ├── css
│   ├── images
│   └── js
└── templates
    ├── accounts
    ├── base.html
    ├── core
    ├── footer.html
    └── navbar.html
```

The more detailed structure can be found [here]()
