from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "contact", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/contact")
def index():
    return render_template("contact.html")