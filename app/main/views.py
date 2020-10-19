from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source
from ..requests import get_sources
# from .forms import

# Views
@main.route("/")
def index():
    """
    View function that returns root page index.html
    """
    sources_list = get_sources()

    return render_template("index.html", sources = sources_list)