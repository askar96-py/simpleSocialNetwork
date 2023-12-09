from flask import Blueprint, render_template, request, redirect, url_for
from app.data_controller import db
from random import randrange


sign = Blueprint('sign', __name__, template_folder='templates', static_folder='static')

@sign.route('/sign', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        new_user = {
            'id' : randrange(1, 100000),
            'username' : request.form['username'],
            'name' : request.form['name'],
            'surname' : request.form['surname'],
            'city' : request.form['city'],
            'age' : request.form['age'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'profession' : request.form['profession']
        }
        db.add_new_user(new_user)
        return redirect('/')
    return render_template('sign.html')