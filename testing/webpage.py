# In webpage.py
from flask import Flask

app = Flask(__name__)

# Define your routes
@app.route('/')
def home():
    return "Hello, World!"

def run_server(debug=False, use_reloader=False):
    app.run(debug=debug, use_reloader=use_reloader)
