import os

class Config:
    """
    Config parent class
    """
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?language=en&apiKey={}"


class ProdConfig(Config):
    """
    Production configuration class. inherits from Config.
    
    Args:
        Config: The parent config class
    """
    pass
class DevConfig(Config):
    """
    Development configuration class. Inherits from Config.

    Args:
        Config: The parent config class
    """
    DEBUG = True

config_options = {
    "development":DevConfig,
    "production":ProdConfig
}