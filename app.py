#  $env:FLASK_ENV = "development"
from unicodedata import name
from flask import Flask, render_template
from markupsafe import escape

from forms.form import TestForm


app = Flask(__name__)

# To escape if HTML is returned by a fonction:
    # from markupsafe import escape

    # @app.route("/<name>")
    # def hello(name):
    #     return f"Hello, {escape(name)}!"


@app.route('/')
def projects():
    test_form = TestForm()
    return render_template('hello.html', form=test_form)


@app.route('/hello/')
@app.route('/hello/<user_name>')
def hello(user_name=None):
    return render_template('hello.html', name=user_name)
