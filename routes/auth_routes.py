from flask import render_template,Blueprint,request,redirect,url_for,flash,session
from services import user_service

auth_bp=Blueprint("auth",__name__)

@auth_bp.route("/signup",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        full_name=request.form["full_name"]
        email=request.form["email"]
        password=request.form["password"]
        
        result=user_service.signup(full_name,email,password)
        
        if result is None:
            flash("Email already exists")
            return render_template("signup.html")
        
        return redirect(url_for("auth.signin"))
     
    return render_template("signup.html")

@auth_bp.route("/signin",methods=["GET","POST"])
def signin():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        user= user_service.signin(email,password)   
        
        if user is None:
            flash("Invalid email or password")
            return render_template("signin.html")
        
        session["user_id"] = user.id
        session["username"] = user.full_name
        
        return redirect(url_for("dash.dashboard"))

    return render_template("signin.html")
