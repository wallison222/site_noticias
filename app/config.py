import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "4c6acf6496dc4ac99481296f10410972e151a4e1afc3b09fe8263fd3c5098782")
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API de notícias (substitua pela sua chave)
    NEWS_API_KEY = os.getenv("NEWS_API_KEY", "dc340114af1f28969bc8edefc0d299e6")
 
# Compare this snippet from app/models.py: