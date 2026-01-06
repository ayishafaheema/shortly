from flask import Flask,render_template
from routes.dashboard_routes import dash_bp
from routes.auth_routes import auth_bp
from routes.redirect_routes import redirect_bp

import os
from extension import db

app=Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))  # ensures project folder
db_path = os.path.join(basedir, "database.db")

app.secret_key = "my_super_secret_key_123"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.register_blueprint(dash_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(redirect_bp)

db.init_app(app)
with app.app_context():
    db.create_all()

print("DATABASE PATH:", db_path)

if __name__=="__main__":
    app.run(debug=True)