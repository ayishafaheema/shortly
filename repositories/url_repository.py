from models.url import Url
from extension import db   

class UrlRepository:

    def get_by_short_code(short_code):
        return Url.query.filter_by(short_code=short_code).first()

    
    def short_code_exists(short_code):
        return Url.query.filter_by(short_code=short_code).first() is not None

    def save(url):
        db.session.add(url)
        db.session.commit()
