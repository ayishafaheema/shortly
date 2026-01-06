from flask import Blueprint, redirect, abort
from services.redirect_service import RedirectService

redirect_bp = Blueprint("redirect", __name__)

@redirect_bp.route("/<short_code>")
def redirect_short_code(short_code):
    long_url = RedirectService.resolve_short_code(short_code)
    
    print("TYPE OF RedirectService:", type(RedirectService))  # 👈 HERE
    print("Redirect request for:", short_code)

    if not long_url:
        abort(404)

    return redirect(long_url)
