from flask import Blueprint, render_template, request, redirect, url_for
from app.data_controller import db

my_profile = Blueprint('my_profile', __name__, template_folder='templates', static_folder='static')

@my_profile.route('/my-profile', methods=["POST","GET"])
def index():
    if request.method == "POST":
        if len(request.form) == 0:
            db.delete_current_user()
            db.set_current_user(None)
            return redirect('/')
        else:
            temp = db.get_current_user()
            print(request.form)
            for k, v in dict(request.form).items():
                if v != "":
                    temp[k] = v
            db.set_current_user(temp)
            return redirect('/')

    return render_template('my_profile.html', data = db.get_current_user())