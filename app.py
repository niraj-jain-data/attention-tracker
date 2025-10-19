from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect("clicks.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS clicks (x INTEGER, y INTEGER)")
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/heatmap")
def heatmap():
    return render_template("heatmap.html")

@app.route("/api/click", methods=["POST"])
def save_click():
    data = request.get_json()
    x, y = data["x"], data["y"]
    conn = sqlite3.connect("clicks.db")
    c = conn.cursor()
    c.execute("INSERT INTO clicks (x, y) VALUES (?, ?)", (x, y))
    conn.commit()
    conn.close()
    return jsonify(success=True)

@app.route("/api/clicks")
def get_clicks():
    conn = sqlite3.connect("clicks.db")
    c = conn.cursor()
    c.execute("SELECT x, y FROM clicks")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"x": x, "y": y} for x, y in rows])

if __name__ == "__main__":
    app.run(debug=True)
