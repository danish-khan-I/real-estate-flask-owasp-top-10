from flask import (
    Blueprint,
    request,
    render_template
)

bp = Blueprint(
    "/", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/", methods=['POST'])
def appointment():
    ### A poorly written code can expose a lot of things specially if the DEBUG mode is left on
    ##  FIX: turn over debug mode!
    age = int(request.form.get("budget", 0))
    fullname = request.form.get('fullname')
    new_age = 0
    if age:
        new_age = age + 1
    return render_template("index.html", budget=new_age,fullname=fullname)