import urllib.request, json

# Get api key and base url
api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]