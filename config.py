import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Config parent class
    """
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWS_API_BASE_URL = "https://newsapi.org/v2/{}?q=%22a%22&language=en&apiKey={}"


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
