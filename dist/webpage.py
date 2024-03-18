from flask import Flask, jsonify, render_template
import csv

app = Flask(__name__)

@app.route("/")
def index():
    """Serve the index HTML file."""
    return render_template("index.html")

@app.route("/data")
def data():
    """Read the CSV file and return its content in JSON format."""
    filename = "sound_levels.csv"
    data = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            try:
                # Ensure that each row has the correct number of columns
                if len(row) == 2:
                    data.append({"timestamp": row[0], "level": float(row[1])})
            except ValueError:
                continue  # Skip rows with conversion errors
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
