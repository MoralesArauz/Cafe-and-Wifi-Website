from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL, Optional

class CafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    map_url = StringField("Map URL", validators=[DataRequired(), URL()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    seats = StringField("Seats", validators=[DataRequired()])
    coffee_price = StringField("Coffee Price", validators=[Optional()])
    has_wifi = BooleanField("WiFi")
    has_sockets = BooleanField("Sockets")
    has_toilet = BooleanField("Toilet")
    can_take_calls = BooleanField("Can Take Calls")
    submit = SubmitField("Add Café")