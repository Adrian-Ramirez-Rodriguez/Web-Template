# app.py
from flask import Flask, render_template, session
from extensions import db, login_manager
from flask_login import login_required
from dotenv import load_dotenv
from socket import socket
from models import User
from auth import auth
from os import getenv

def create_app():
    app = Flask(__name__)
    
    load_dotenv('.env')

    app.config['VALID_CHARACTERS'] = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['PASS_MINMAX'] = (10, 128)
    app.config['NAME_MINMAX'] = (3, 24)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(auth)
    
    @app.route('/')
    @login_required
    def index():
        return render_template('index.html', session=session)
    
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            secure_admin_account()
    
    return app

def find_port():
    s = socket()
    s.bind(('', 0))
    return s.getsockname()[1]

def secure_admin_account():
    # `werkzeug.security` is imported inside
    # the function to avoid circular imports
    from werkzeug.security import generate_password_hash

    print(f'\033[91mAdmin Account Not Found\033[00m')

    _username = getenv('_ADMINISTRATOR_USERNAME')
    _password = getenv('_ADMINISTRATOR_PASSWORD')
    hashed_password = generate_password_hash(_password)

    new_user = User(username=_username, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()

    print(f'\033[92mAdmin Account Created\033[00m')

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=find_port(), debug=True)
