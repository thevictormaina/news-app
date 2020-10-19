import urllib.request, json
from .models import Source, Article

# Get api key and base url
api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]

    print(base_url)

def api_request(endpoint):
    """
    Function to call list of sources from api
    """

    if endpoint == "sources":
        request_url = base_url.format(endpoint, api_key)
    elif endpoint == "top-headlines":
        request_url = base_url.format(endpoint, api_key) + "&category=general"
    else:
        request_url = None

    print(api_key, "\n", request_url)

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

    if api_response["sources"]:
        for source in api_response["sources"]:
            id = source.get("id")
            name = source.get("name")
            description = source.get("description")
            url = source.get("url")
            category = source.get("category")
            country = source.get("country")

            result = Source(id, name, description, url, category, country)

            results.append(result)

    elif api_response["articles"]:
        for article in api_response["articles"]:
            source_id = article.get("source.id")
            source_name = article.get("source.name")
            author = article.get("author")
            title = article.get("title")
            description = article.get("description")
            url = article.get("url")
            url_to_image = article.get("urlToImage")
            published_at = article.get("publishedAt")

            result = Article(source_id, source_name, author, title, description, url, url_to_image, published_at)

            results.append(result)

    return results

