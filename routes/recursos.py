from flask import Blueprint, render_template, redirect, url_for
from forms.recursosCreateForms import recursosCreateForm
from forms.recursosUpdateForms import recursosUpdateForm
from flask_login import login_user, login_required, logout_user, current_user
from utils.bcryptService import bcrypt
from models.user import User
from utils.db import db

Recursos = Blueprint("Recursos", __name__, url_prefix="/Recursos")



@Recursos.route("/")
@login_required
def home():
    return render_template("RRHH/home.html")


@Recursos.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = recursosCreateForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        status = form.status.data
        rank = form.rank.data
        hashed_password = bcrypt.generate_password_hash(password)
        newRecursos = User(username, hashed_password, status, rank)
        db.session.add(newRecursos)
        db.session.commit()
        return redirect(url_for("Recursos.home"))
    return render_template("RRHH/create.html", form=form)


@Recursos.route("/recursos", methods=["GET", "POST"])
@login_required
def recursos():
    recursos = User.query.all()
    return render_template("RRHH/recursos.html", recursos=recursos)


@Recursos.route("/update/<int:RecursosId>", methods=["GET", "POST"])
@login_required
def update(RecursosId):
    currentRecursos = User.query.filter_by(id=RecursosId).first()
    form = recursosUpdateForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        status = form.status.data
        rank = form.rank.data
        hashed_password = bcrypt.generate_password_hash(password)
        currentRecursos.username = username
        currentRecursos.password = hashed_password
        currentRecursos.status = status
        currentRecursos.rank = rank
        db.session.add(currentRecursos)
        db.session.commit()
        return redirect(url_for("Recursos.recursos"))
    return render_template("RRHH/update.html",form=form, RecursosId=currentRecursos)


@Recursos.route("/delete/<int:RecursosId>")
@login_required
def delete(RecursosId):
    currentRecursos = User.query.filter_by(id=RecursosId).first()
    db.session.delete(currentRecursos)
    db.session.commit()
    return redirect(url_for("Recursos.recursos"))