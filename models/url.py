from extension import db
from datetime import datetime


class Url(db.Model):
    __tablename__="url"

    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    long_url=db.Column(db.Text,nullable=False)
    short_code=db.Column(db.String(20),unique=True,nullable=False)
    click_count=db.Column(db.Integer,default=0,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    expiry_at=db.Column(db.DateTime,nullable=True)











