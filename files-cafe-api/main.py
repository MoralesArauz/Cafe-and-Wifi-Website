from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    # Remove the extra column from the function __dict__
    random_cafe.__dict__.pop("_sa_instance_state")
    return jsonify({"Cafe" : random_cafe.__dict__})

@app.route("/all")

def all():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
    cafe_list = []
    for cafe in all_cafes:
        cafe.__dict__.pop("_sa_instance_state")
        cafe_list.append(cafe.__dict__)

    return jsonify({"cafes": cafe_list})

# HTTP GET - Read Record

@app.route("/search")
def search():
    location = request.args.get("loc", "").strip()

    all_cafes = db.session.query(Cafe).filter_by(location=location).all()
    if all_cafes:
        cafe_list = []
        for cafe in all_cafes:
            cafe.__dict__.pop("_sa_instance_state")
            cafe_list.append(cafe.__dict__)

        return jsonify({"cafes": cafe_list})
    else:
        return jsonify({
            "error": {
                "Not Found": "Sorry, we don't have a cafe at that location"
            }
        })

# HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("loc"),
        has_sockets=bool(request.args.get("sockets")),
        has_toilet=bool(request.args.get("toilet")),
        has_wifi=bool(request.args.get("wifi")),
        can_take_calls=bool(request.args.get("calls")),
        seats=request.args.get("seats"),
        coffee_price=request.args.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Cafe with that ID not found."}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."})
        else:
            return jsonify(error={"Not Found": "Cafe with that ID not found."}), 404
    else:
        return jsonify(error={"Forbidden": "You don't have permission to delete a cafe."}), 403

if __name__ == '__main__':
    app.run(debug=True)
