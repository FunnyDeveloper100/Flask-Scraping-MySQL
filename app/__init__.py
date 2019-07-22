from app.db import db
from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from config import settings
from app.domain import domain_app


""" create flask app """
application = Flask(__name__)


""" set config settings """
application.config.from_object(settings)


""" set database """
db.init_app(application)
migrate = Migrate(application, db)


""" register bluprint """
application.register_blueprint(domain_app.domain_app)

""" error page """
@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


""" index """
@application.route('/')
def index():
    return redirect('/domain')
