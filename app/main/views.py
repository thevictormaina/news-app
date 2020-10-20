from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source
from ..requests import api_request
# from .forms import

# Views
@main.route("/")
def index():
    """
    View function that returns root page index.html
    """
    sources_list = api_request("sources")
    headlines = api_request("top-headlines")

    return render_template("index.html", sources = sources_list, headlines = headlines)