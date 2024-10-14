# auth/routes.py
from flask import Blueprint, render_template, request, redirect, session, current_app
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from extensions import db, login_manager
from models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            session['username'] = user.username
            return redirect('/')
        return render_template('login.html', error='> Invalid username or password')
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    VALID_CHARACTERS = f"{current_app.config['VALID_CHARACTERS']}"
    NAME_MINMAX = current_app.config['NAME_MINMAX']
    PASS_MINMAX = current_app.config['PASS_MINMAX']

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        error = _invalid_user_register(username, password, confirm_password, VALID_CHARACTERS, NAME_MINMAX, PASS_MINMAX)
        if error:
            return render_template('register.html', error=error)

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')
    return render_template('register.html')

def _invalid_user_register(username, password, confirm_password, valid_characters, name_minmax, pass_minmax):
    username_length = len(username)
    password_length = len(password)

    user_exists_error = User.query.filter_by(username=username).first()
    pass_match_error = password != confirm_password

    pass_len_error = password_length not in range(pass_minmax[0], pass_minmax[1] + 1)
    name_len_error = username_length not in range(name_minmax[0], name_minmax[1] + 1)
    
    for char in username:
        if char not in valid_characters:
            return '> Invalid Username or Invalid Characters'

    if user_exists_error:
        return '> Username already taken'
    
    if name_len_error:
        return f'> Usernames must be between {name_minmax[0]} - {name_minmax[1]} characters long'
    
    if pass_match_error:
        return '> Passwords do not match'
    
    if pass_len_error:
        return f'> Passwords must be between {pass_minmax[0]} - {pass_minmax[1]} characters long'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('username', None)
    return redirect('/')
