class Source:
    """
    Class to define structure and methods of news sources
    """
    def __init__(self, id, name, description, url, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

class Article:
    """
    Class to define structure and methods of articles
    """
    def __init__(self, source_id, source_name, author, title, description, url, url_to_image, published_at):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at