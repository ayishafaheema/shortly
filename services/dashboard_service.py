from datetime import datetime,timedelta
import string,secrets
from models.url import Url
from repositories.url_repository import UrlRepository



class DashboardService:
    
    @staticmethod
    def create_short_code(user_id,long_url,custom_name=None,expiry=None):
        
        if custom_name:
            short_code=DashboardService.validate_custom_name(custom_name)
        else:
            short_code=DashboardService.generate_random_code()
            
        expiry_at=DashboardService.calculate_expiry(expiry)
        
        url = Url(
                long_url=long_url,
                short_code=short_code,
                expiry_at=expiry_at,
                click_count=0,
                user_id=user_id
            )
        
    
        UrlRepository.save(url)

        return url


    @staticmethod
    def validate_custom_name(custom_name):
        if UrlRepository.short_code_exists(custom_name):
            raise ValueError("Custom short name already exists")
        return custom_name

        
    @staticmethod
    def generate_random_code(length=6):
        characters=string.ascii_letters+string.digits
        
        while True:
            code= ''.join(secrets.choice(characters)for _ in range(length))
            
            if not UrlRepository.short_code_exists(code):
                return code
            
            
    @staticmethod
    def calculate_expiry(expiry):
        if not expiry or expiry == "never":
            return None
            
        now=datetime.utcnow()
        
        if expiry=="1m":
            return now + timedelta(minutes=1)
        elif expiry=="5m":
            return now + timedelta(minutes=5)
        elif expiry=="1d":  
            return now + timedelta(days=1)
        
        else:
            raise ValueError("Invalid expiry option")
            
            
                    

