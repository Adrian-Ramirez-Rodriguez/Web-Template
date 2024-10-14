# WebTemplate

WebTemplate is a Flask-based web application designed for user authentication, registration, and session management. This project provides a solid foundation for building web applications with user authentication features.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

## Features
- User registration and login functionality.
- Password hashing for secure password storage.
- Session management using Flask-Login.
- Basic styling using CSS.
- Built with Flask and SQLAlchemy for ORM.

## Project Structure
```
WebTemplate
│   .env (* manual)
│   app.py
│   extensions.py
│   LICENSE
│   models.py
│   outline
│   README.md
│   requirements.txt
│
├───auth
│       routes.py
│       __init__.py
│
├───instance (* generated)
│       users.db (* generated)
│
├───static
│       auth.css
│       style.css
│
├───templates
│       index.html
│       login.html
│       register.html
│
└───...
```

### File Descriptions
- **app.py**: The main 'entry point' of the application that initializes the Flask app and its configurations.
- **extensions.py**: Contains the setup for database and login manager.
- **models.py**: Defines the database models, including the User model.
- **auth/**: Directory containing authentication routes.
  - **routes.py**: Defines the routes for login, registration, and logout.
  - **__init__.py**: Initializes the auth module.
- **instance/**: Contains the SQLite database (`users.db`).
- **static/**: Directory for static files, including CSS styles.
- **templates/**: Contains HTML templates for rendering the web pages.
- **requirements.txt**: Lists the project dependencies.
- **.env**: Environment variables for sensitive information. (**Create this manually!**)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Adrian-Ramirez-Rodriguez/WebTemplate.git
   cd WebTemplate
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up the environment variables:
   - Create a `.env` file in the root directory and add your configuration ([see below](#environment-variables)).

2. Run the application:
   ```bash
   python app.py
   ```

3. Access the application in your browser at `http://localhost:port`. Where the `port` is found using the `find_port` function in `app.py`.

## Environment Variables
Add the following variables to your `.env` file:
```env
SECRET_KEY="your_random_secret_key_here"
_ADMINISTRATOR_USERNAME="Admin"
_ADMINISTRATOR_PASSWORD="your_secure_password_here"
```

## Running the Application
- The application will start with debug mode enabled for development purposes. You can access the application at `http://localhost:port`.
- The first time you run the app, it will check for an admin account. If it doesn’t exist, it will create one using the credentials defined in your `.env` file.

## Contributing
Thank you for your interest in contributing to `WebTemplate`! At this time, I'm are not accepting contributions or pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
