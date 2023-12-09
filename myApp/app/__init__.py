from flask import Flask
from app import main
from app.auth import login, sign_in, my_profile


def create_app():
    app = Flask(__name__)

    # Регистрация Blueprint'ов
    app.register_blueprint(main.main, url_prefix='/')
    app.register_blueprint(login.login, url_prefix='/')
    app.register_blueprint(sign_in.sign, url_prefix='/')
    app.register_blueprint(my_profile.my_profile, url_prefix='/')

    return app
