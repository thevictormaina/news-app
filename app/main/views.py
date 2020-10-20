from flask import render_template, request, redirect, url_for
from . import main
from ..models import Source
from ..requests import api_request, request_source
# from .forms import

# Views
@main.route("/")
def index():
    """
    View function that returns root page index.html
    """
    sources_list = api_request("sources")
    headlines = api_request("top-headlines")

    print(request_source("abc-news"))

    return render_template("index.html", sources = sources_list, headlines = headlines)

@main.route("/source/<id>")
def source(id):
    """
    View function that returns page of new source
    """
    source_tuple = request_source(id)
    source_object = source_tuple[0]
    source_articles = source_tuple[1]

    return render_template("source.html", source = source_object, articles = source_articles)