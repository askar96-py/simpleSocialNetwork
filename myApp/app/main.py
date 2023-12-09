from flask import Blueprint, render_template
from app.data_controller import db

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/home')
@main.route('/')
def index():
    return render_template('users.html', users= db.get_user_list(), current_user= db.get_current_user())

@main.route('/id/<int:id>')
def profile(id):
    users = db.get_user_list()
    for i in users:
        if i['id'] == id:
            return render_template('profile.html', data = i)
    return render_template('users.html', users=db.get_user_list(), current_user= db.get_current_user())
