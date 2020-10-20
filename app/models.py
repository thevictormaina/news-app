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
    
    def format_time(self):
        """
        Method to make published_at more readable

        Args:
            self
            api_time: time value received from News API
        """
        months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

        published_at_split = self.published_at.split("T")
        date_split = published_at_split[0].split("-")
        time_split = published_at_split[1].split(":")

        formatted_time = time_split[0] + ":" + time_split[1] # hour:minute, 24-hour time format

        formatted_year = date_split[0]
        formatted_month = months_list[ int(date_split[1]) - 1 ]
        formatted_date = date_split[2]

        date = "{} {} {}, {}".format(formatted_time, formatted_month, formatted_date, formatted_year)

        return date


        