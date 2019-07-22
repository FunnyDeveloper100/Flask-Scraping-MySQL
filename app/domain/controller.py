from flask import Blueprint, request, redirect, render_template, flash, url_for
from app.db import db
from .models import Domain


""" create domain_app for blueprint """
domain_app = Blueprint('domain_app', __name__, url_prefix='/domain')


@domain_app.route('/')
def domains():
    """ get all domain list with pagination """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    domain_data = Domain.query.paginate(page, per_page, False)

    next_url = url_for('domain_app.domains', page=domain_data.next_num) \
        if domain_data.has_next else None
    prev_url = url_for('domain_app.domains', page=domain_data.prev_num) \
        if domain_data.has_prev else None

    return render_template('index.html', domain_data=domain_data.items,
                           next_url=next_url, prev_url=prev_url)


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
