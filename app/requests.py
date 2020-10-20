import urllib.request
import json
from .models import Source, Article

# Get api key and base url
api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]


def api_request(endpoint):
    """
    Function to call list of sources from api
    """

    if endpoint == "sources":
        request_url = base_url.format(endpoint, api_key)
    elif endpoint == "top-headlines":
        # Using everything endpoint to enable removing articles not written in English
        request_url = base_url.format(
            "everything", api_key) + "&sortBy=publishedAt&pageSize=35"
    else:
        request_url = None

    with urllib.request.urlopen(request_url) as url:
        request_data = url.read()
        api_response = json.loads(request_data)

        response_list = None

        if api_response["status"] == "ok":
            response_list = process_response(api_response)

        return response_list


def process_response(api_response):
    """
    Function that turn returns from api into list of objects
    """
    results = []

    if api_response.get("sources"):
        sources = api_response.get("sources")
        for source in sources:
            id = source.get("id")
            name = source.get("name")
            description = source.get("description")
            url = source.get("url")
            category = source.get("category")
            country = source.get("country")

            result = Source(id, name, description, url, category, country)

            results.append(result)

    elif api_response.get("articles"):
        articles = api_response.get("articles")

        for article in articles:
            source = article.get("source")
            source_id = source.get("id")
            source_name = source.get("name")

            if article["author"] == None:
                author = source_name
            else:
                author = article.get("author")

            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            url_to_image = article.get("urlToImage")
            published_at = article.get("publishedAt")

            result = Article(source_id, source_name, author, title,
                             description, url, url_to_image, published_at)

            if result.url_to_image:
                results.append(result)

    return results

def request_source(id):
    """
    Returns tuple with source object and articles by id
    """
    # Create source object
    sources = api_request("sources")

    # Search sources list by id for specific source
    source_result = None

    for source in sources:
        if source.id == id:
            source_result = source

    # Search API for all articles of source

    request_url = base_url.format(
        "everything", api_key) + f"&sources={id}&sortBy=publishedAt&pageSize=35"

    with urllib.request.urlopen(request_url) as url:
        request_data = url.read()
        api_response = json.loads(request_data)

        source_articles = None

        if api_response["status"] == "ok":
            source_articles = process_response(api_response)

    return source_result, source_articles
