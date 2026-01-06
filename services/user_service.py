from werkzeug.security import generate_password_hash,check_password_hash
from models.user import User 
from extension import db


    
def signup(full_name,email,password):
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return None
    
    hashed_password = generate_password_hash(password)

    user=User(
        full_name=full_name,
        email=email,
        password=hashed_password
    )
    db.session.add(user)
    db.session.commit()

    return user

def signin(email,password):
    user=User.query.filter_by(email=email).first()

    if user is None:
       return None
    if not check_password_hash(user.password,password):
       return None
    return user

    