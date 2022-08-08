from unicodedata import name
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


# To escape if HTML is returned by a fonction:
    # from markupsafe import escape

    # @app.route("/<name>")
    # def hello(name):
    #     return f"Hello, {escape(name)}!"

@app.route('/')
def projects():
    return 'The HOME PAGE!'
