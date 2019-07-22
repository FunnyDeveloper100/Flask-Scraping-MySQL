from flask import Blueprint, request, redirect, render_template, flash, url_for
from app.db import db

""" create domain_app for blueprint """
domain_app = Blueprint('domain_app', __name__, url_prefix='/domain')

@domain_app.route('/')
def domains():
    """ get all domain list """

@domain_app.route('/insert', methods=['POST'])
def insert():
    """ insert new domain to database """

@domain_app.route('/delete/<string:id>')
def delete(id):
    """ delete one domain by id """

@domain_app.route('/update', methods=['POST'])
def update():
    """ update existing domain """

@domain_app.route('/search')
def search():
    """ search domain data by keywords """

