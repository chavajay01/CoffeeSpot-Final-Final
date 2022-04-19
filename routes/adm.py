from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from forms.registerForm import RegisterForm
from forms.loginForm import LoginForm
from utils.bcryptService import bcrypt
from models.user import User
from utils.db import db

adm = Blueprint("adm", __name__)

@adm.route("/")
@login_required
def home():
    userList = None
    if "admin" in current_user.user:
        # es un admin
        userList = User.query.all()
    else:
        # es un user
        userList = list((User.query.filter_by(id=current_user.id).first(),))
    return render_template("adm/jefe.html", user=current_user, userList=userList)
