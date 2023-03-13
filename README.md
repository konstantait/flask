# [Flask Login](https://github.com/konstantait) Example

**[Flask Login](https://github.com/konstantait)** easy authentication and authorization in Flask example with modular structure using blueprints, app factory pattern, dual configuration profile 
<br />

> Features

- Up-to-date [dependencies](./requirements.txt): **Python 3.10.6 , Flask 2.2.3 , Werkzeug 2.2.3**
- DBMS: SQLite (development) 
- DB Tools: SQLAlchemy ORM, Flask-Migrate (schema migrations)
- Modular design with **Blueprints**, simple codebase
- Session-Based authentication (via **flask_login**)
<br />

> Links

- [Flask Login](https://github.com/konstantait) - product page
<br />

## How to use it

```bash
$ # Ngork installation for external access using
$ curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
  sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
  echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
  sudo tee /etc/apt/sources.list.d/ngrok.list && \
  sudo apt update && sudo apt install ngrok
$ ngrok config add-authtoken TOKEN
$ ngrok http 5000
$
$ # Get the code
$ git clone https://github.com/konstantait
$ cd flask
$
$ # Virtualenv modules installation
$ virtualenv env
$ source env/bin/activate
$
$ # Install modules
$ pip3 install -r requirements.txt
$
$ # Start the application (development mode)
$ flask --app run.py run --debug
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
$ # or external access using ngork
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Code-base structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production), and an intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- routes.py                 # Define app routes
   |    |
   |    |-- auth/                         # Handles auth routes (login and register)
   |    |    |-- routes.py                 # Define authentication routes  
   |    |    |-- models.py                 # Defines models  
   |    |    |-- utils.py                  # Define hash, salt and verify passwords 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |    |    |-- includes/                 # HTML chunks and components
   |    |    |    |-- *.html               #
   |    |    |
   |    |    |-- layouts/                   # Master pages
   |    |    |    |-- base.html             # Used by common pages
   |    |    |
   |    |    |-- accounts/                  # Authentication pages
   |    |    |    |-- login.html            # Login page
   |    |    |    |-- registration.html     # Register page
   |    |    |
   |    |    |-- home/                      # UI Kit Pages
   |    |         |-- index.html            # Index page
   |    |         |-- profile.html          # User profile page
   |    |         |-- *.html                # All other pages
   |    |    
   |  config.py                             # Set up the app
   |    __init__.py                         # Initialize the app
   |
   |-- requirements.txt                     # Development modules
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- run.py                               # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The offcial website

<br />