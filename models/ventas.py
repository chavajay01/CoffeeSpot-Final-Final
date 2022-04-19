from utils.db import db


class ventitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __init__(self, productId, description, price, cantidad) -> None:
        self.productId = productId
        self.description = description
        self.price = price
        self.cantidad = cantidad

    def __repr__(self) -> str:
        return f"Ventas({self.id}, {self.productId}, '{self.description}', '{self.price}','{self.cantidad}')"