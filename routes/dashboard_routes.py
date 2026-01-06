from flask import Flask,render_template,Blueprint,request,redirect,url_for
from services.dashboard_service import DashboardService
from flask import session


dash_bp=Blueprint("dash",__name__)

@dash_bp.route("/dashboard",methods=["GET","POST"])
def dashboard():
    if request.method=="POST":
        
        if "user_id" not in session:
            return redirect(url_for("auth.signin"))
        user_id = session.get("user_id")
    
        long_url = request.form.get("long_url")
        custom_name = request.form.get("custom_name")
        expiry = request.form.get("expiry")
        
        
        url=DashboardService.create_short_code(user_id,long_url,custom_name,expiry)
        return render_template(
            "dashboard.html",
            short_code=url.short_code
        )

    return render_template("dashboard.html")

