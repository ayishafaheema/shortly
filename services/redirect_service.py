from datetime import datetime
from repositories.url_repository import UrlRepository
from extension import db



class RedirectService:
    
    @staticmethod
    def resolve_short_code(short_code):
        url=UrlRepository.get_by_short_code(short_code)
        
        if not url:
            return None
        if url.expiry_at and url.expiry_at<datetime.utcnow():
            return None
        
        url.click_count+=1
        db.session.commit()
            
        return url.long_url    