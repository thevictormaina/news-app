from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source
# from ..requests import 
# from .forms import

# Views
@main.route("/")
def index():
    """
    Function to return root page
    """
    return render_template("index.html")