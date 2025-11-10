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

@app.route("/read")
def read():
    return render_template("read.html")
@app.route("/read2")
def read2():
    return render_template("read2.html")

@app.route("/read3")
def read3():
    return render_template("read3.html")
@app.route("/read4")
def read4():
    return render_template("read4.html")

@app.route("/read5")
def read5():
    return render_template("read5.html")

@app.route("/read6")
def read6():
    return render_template("read6.html")

@app.route("/read7")
def read7():
    return render_template("read7.html")

@app.route("/read8")
def read8():
    return render_template("read8.html")

@app.route("/read9")   
def read9():
    return render_template("read9.html")

@app.route("/read10")   
def read10():
    return render_template("read10.html")
@app.route("/api/click", methods=["POST"])
def save_click():
    data = request.get_json()
    x, y = data["x"], data["y"]
    print("Before ")
    conn = sqlite3.connect("clicks.db")
    print("After here")
    print(conn)
    c = conn.cursor()
    c.execute("INSERT INTO clicks (x, y) VALUES (?, ?)", (x, y))
    conn.commit()
    conn.close()
    return jsonify(success=True)

@app.route("/api/clicks")
def get_clicks():
    print("Checking")
    conn = sqlite3.connect("clicks.db")
    c = conn.cursor()
    c.execute("SELECT x, y FROM clicks")
    rows = c.fetchall()
    conn.close()
    return jsonify([{"x": x, "y": y} for x, y in rows])

if __name__ == "__main__":
    app.run(debug=True)
