from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from utils.db import db
from models.user import User


todolist = Blueprint("todolist", __name__, url_prefix="/todolist")


@todolist.route("/")
@login_required
def home():
    userList = None
    if "admin" in current_user.rank:
        # es un admin
        userList = User.query.all()
    else:
        # es un user
        userList = list((User.query.filter_by(id=current_user.id).first(),))
    return render_template("Finanzas/Finanzas.html", user=current_user, userList=userList)




