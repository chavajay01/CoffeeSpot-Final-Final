from flask import Blueprint, render_template, redirect, url_for
from forms.ventasCreateForms import ventasCreateForm
from forms.ventasUpdateForms import ventasUpdateForm
from flask_login import login_user, login_required, logout_user, current_user
from models.ventas import ventitas
from utils.db import db

Ventas = Blueprint("Ventas", __name__, url_prefix="/Ventas")



@Ventas.route("/")
@login_required
def home():
    return render_template("Ventas/home.html")
    
    
@Ventas.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = ventasCreateForm()
    if form.validate_on_submit():
        productId = form.productId.data
        description = form.description.data
        price = form.price.data
        cantidad = form.cantidad.data
        newVentas = ventitas(productId, description, price, cantidad)
        db.session.add(newVentas)
        db.session.commit()
        return redirect(url_for("Ventas.home"))
    return render_template("Ventas/create.html", form=form)


@Ventas.route("/ventas", methods=["GET", "POST"])
@login_required
def ventas():
    vent = ventitas.query.all()
    return render_template("Ventas/ventas.html", vent=vent)

@Ventas.route("/update/<int:ventasId>", methods=["GET", "POST"])
@login_required
def update(ventasId):
    currentVentas = ventitas.query.filter_by(id=ventasId).first()
    form = ventasUpdateForm()
    if form.validate_on_submit():
        productId = form.productId.data
        description = form.description.data
        price = form.price.data
        cantidad = form.cantidad.data
        currentVentas.productId = productId
        currentVentas.description = description
        currentVentas.price = price
        currentVentas.cantidad = cantidad
        db.session.add(currentVentas)
        db.session.commit()
        return redirect(url_for("Ventas.ventas"))
    return render_template("Ventas/update.html",form=form, ventasId=currentVentas)


@Ventas.route("/delete/<int:ventasId>")
@login_required
def delete(ventasId):
    currentVentas = ventitas.query.filter_by(id=ventasId).first()
    db.session.delete(currentVentas)
    db.session.commit()
    return redirect(url_for("Ventas.ventas"))

@Ventas.route("/VT", methods=["GET", "POST"])
@login_required
def VT():
    vent = ventitas.query.all()
    return render_template("Finanzas/ventastotales.html", vent=vent)


@Ventas.route("/Finanzas")
@login_required
def finanzas():
    return render_template("Finanzas/Finanzas.html")
