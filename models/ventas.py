from utils.db import db


class Ventas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(200), nullable=False)
    Fecha = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, producto, code, Fecha, price) -> None:
        self.producto = producto
        self.code = code
        self.Fecha = Fecha
        self.price = price

    def __repr__(self) -> str:
        return f"Inventario({self.id}, {self.producto}, '{self.Fecha}', '{self.code}', '{self.price}')"