# ☕ Cafe and Wifi Website

A Flask-based web application that helps users discover and share work-friendly cafés with WiFi across London. Built with Flask, SQLAlchemy, Bootstrap, and a custom API.

## 🚀 Features

- Search cafés by location
- View all cafés with images, prices, and amenities
- Add new cafés via a secure form
- Clickable cards for detailed café views
- Responsive design with Bootstrap
- API integration for dynamic data

## 🧰 Tech Stack

- **Frontend:** Flask, Jinja2, Bootstrap
- **Backend:** Flask API, SQLite, SQLAlchemy
- **Forms:** Flask-WTF
- **Version Control:** Git & GitHub

## 📁 Project Structure

```
Cafe-and-Wifi-Website/
├── flask-cafe-website/   # Frontend Flask app
│   ├── templates/
│   ├── static/
│   ├── app.py
│   └── forms.py
├── files-cafe-api/       # API backend
│   ├── main.py
│   └── cafe.db
```

## 🛠️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/MoralesArauz/cafe-and-wifi-website.git
   cd cafe-and-wifi-website
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Run the API:
   ```bash
   cd files-cafe-api
   python main.py
   ```

4. Run the frontend:
   ```bash
   cd ../flask-cafe-website
   python app.py
   ```

5. Visit `http://127.0.0.1:5001` to explore the app.

## ✨ Future Improvements

- Add user authentication
- Enable café ratings and reviews
- Integrate map view with markers
- Filter cafés by amenities

## 📸 Screenshots

_Add screenshots of the homepage, café cards, and add form here._

## 📄 License

MIT License © 2025 Adrian Morales
