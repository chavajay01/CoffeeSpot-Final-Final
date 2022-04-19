from flask import Blueprint, render_template, redirect, url_for
from forms.ventasCreateForms import ventasCreateForm
from models.ventas import Ventas
from utils.db import db

Ventas = Blueprint("Ventas", __name__, url_prefix="/Ventas")



@Ventas.route("/")
def home():
    return render_template("Ventas/home.html")
    
    
@Ventas.route("/create", methods=["GET", "POST"])
def create():
    form = ventasCreateForm()
    if form.validate_on_submit():
        producto = form.producto.data
        code = form.code.data
        Fecha = form.Fecha.data
        price = form.price.data
        newVenta = Ventas(producto, code, Fecha, price)
        db.session.add(newVenta)
        db.session.commit()
        return redirect(url_for("Ventas.home"))
    return render_template("Ventas/create.html", form=form)


@Ventas.route("/ventas", methods=["GET", "POST"])
def ventas():
    vent = Ventas.query.all()
    return render_template("Ventas/ventas.html", vent=vent)


@Ventas.route("/delete/<int:ventasId>")
def delete(ventasId):
    currentVentas = Ventas.query.filter_by(id=ventasId).first()
    db.session.delete(currentVentas)
    db.session.commit()
    return redirect(url_for("Ventas.venta"))

