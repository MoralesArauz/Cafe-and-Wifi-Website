from flask import Flask, render_template, redirect, request,flash, url_for
import requests
from datetime import datetime
from forms import CafeForm


app = Flask(__name__)
app.secret_key = "your-secret-key"  # Required for CSRF protection

# Inject current year for footer
@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# View all cafés
@app.route("/view-all")
def show_all_cafes():
    response = requests.get("http://localhost:5000/all")
    cafes = response.json().get("cafes", [])
    return render_template("cafes.html", cafes=cafes)

# Search cafés by location
@app.route("/search-results")
def search_results():
    location = request.args.get("loc", "")
    response = requests.get(f"http://localhost:5000/search?loc={location}")
    cafes = response.json().get("cafes", [])
    return render_template("cafes.html", cafes=cafes)

# View single café detail
@app.route("/cafe/<int:cafe_id>")
def cafe_detail(cafe_id):
    response = requests.get("http://localhost:5000/all")
    cafes = response.json().get("cafes", [])
    cafe = next((c for c in cafes if c["id"] == cafe_id), None)
    if cafe:
        return render_template("cafe_detail.html", cafe=cafe)
    return render_template("404.html"), 404


@app.route("/add-place", methods=["GET", "POST"])
def add_place():
    form = CafeForm()
    if form.validate_on_submit():
        params = {
            "name": form.name.data,
            "map_url": form.map_url.data,
            "img_url": form.img_url.data,
            "loc": form.location.data,
            "seats": form.seats.data,
            "coffee_price": form.coffee_price.data,
            "wifi": int(form.has_wifi.data),
            "sockets": int(form.has_sockets.data),
            "toilet": int(form.has_toilet.data),
            "calls": int(form.can_take_calls.data),
        }
        response = requests.post("http://127.0.0.1:5000/add", params=params)
        success = response.json().get("response", {}).get("success")
        if success:
            flash("✅ Café added successfully!")
            return redirect(url_for("home"))
    return render_template("add_place.html", form=form)

# Optional: Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(port=5001,debug=True)