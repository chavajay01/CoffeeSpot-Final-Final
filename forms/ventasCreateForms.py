from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class ventasCreateForm(FlaskForm):
    producto = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Nombre del producto"},
    )

    code = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Codigo del producto"},
    )

    Fecha = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Fecha"},
    )
    
    price = StringField(
        validators=[
            InputRequired(),
            Length(min=1, max=200),
        ],
        render_kw={"placeholder": "Precio"},
    )
    
    submit = SubmitField("create task")