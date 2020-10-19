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

def get_sources():
    """
    Function to call list of sources from api
    """

    source_url = base_url.format("sources", api_key)

    print(api_key, "\n", source_url)

    with urllib.request.urlopen(source_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        sources_results = None

        if search_response["sources"]:
            sources_results = process_source_results(search_response["sources"])
        
        return sources_results

def process_source_results(result_list):
    """
    Function that turn returns from api into list of objects
    """
    results = []

    for source in result_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        url = source.get("url")
        category = source.get("category")
        country = source.get("country")
        source = Source(id, name, description, url, category, country)

        results.append(source)
    
    return results

