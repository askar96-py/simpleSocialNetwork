from flask import Blueprint, render_template, request, redirect, url_for
from app.data_controller import db

login = Blueprint('login', __name__, template_folder='templates', static_folder='static')

@login.route('/login', methods=["POST","GET"])
def login_view():
    alert = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if db.check_user_data(username, password):
            print(len(request.form))
            return redirect('/')
        alert = 'LOL'
    return render_template('login.html', alert=alert)
    