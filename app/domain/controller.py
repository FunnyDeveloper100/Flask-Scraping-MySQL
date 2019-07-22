from flask import Blueprint, request, redirect, render_template, flash, url_for
from app.db import db
from .models import Domain, Search, results


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
    if request.method == 'POST':
        domain = request.form['domain']
        first_seen = int(request.form['first_seen'])
        last_seen = int(request.form['last_seen'])
        etld = request.form['etld']

        domain = Domain(domain, first_seen, last_seen, etld)
        db.session.add(domain)
        db.session.commit()
        flash('Inserted new domain data successfully')
    return redirect('/')


@domain_app.route('/delete/<string:id>')
def delete(id):
    """ delete one domain by id """
    try:
        domain = Domain.query.filter_by(id=id).first()
        if domain is not None:
            Domain.query.filter_by(id=id).delete()
            db.session.commit()
            flash(f'Deleted domain by id {id} successfully')
        else:
            flash(f'Failed deleting domain by id {id}')

        return redirect('/')
    except:
        flash(f'Raised an error while deleting domain by {id}')
        return redirect('/')


@domain_app.route('/update', methods=['POST'])
def update():
    """ update existing domain """
    if request.method == 'POST':
        id = request.form['id']
        item = Domain.query.filter_by(id=id).first()
        item.domain = request.form['domain']
        item.first_seen = int(request.form['first_seen'])
        item.last_seen = int(request.form['last_seen'])
        item.etld = request.form['etld']

        db.session.commit()
        flash('Updated successfully!')
    return redirect('/')


def save_search(keyword, domains):
    search = Search(keyword)
    for domain in domains:
        search.domain.append(domain)
    db.session.add(search)
    db.session.commit()


@domain_app.route('/search')
def search():
    """ search domain data by keywords """
    keyword = request.args.get('keyword')

    if (keyword is None):
        flash('No search keywords. Pleaase input keywords!')
        return redirect('/')
    else:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        query = Domain.query
        results = query.filter(
            Domain.domain.like(f'%{keyword}%') |
            Domain.etld.like(f'%{keyword}%') |
            Domain.first_seen.like(f'%{keyword}%') |
            Domain.last_seen.like(f'%{keyword}%') |
            Domain.time_date_imported.like(f'%{keyword}%')
        ).limit(per_page).offset((page - 1) * per_page)

        next_url = url_for('domain_app.search', page=page + 1, keyword=keyword) \
            if results.count() >= per_page else None
        prev_url = url_for('domain_app.search', page=page - 1, keyword=keyword) \
            if page > 1 else None

        if results.count() < 0:
            flash('No data to show by the keyword.')
            return redirect('/')
        else:
            save_search(keyword, results)
            return render_template('index.html', domain_data=results,
                                   next_url=next_url, prev_url=prev_url, keyword=keyword)

@domain_app.route('/search_list')
def search_list():
    search_list = Search.query.all()
    return render_template('search_list.html', search_list=search_list)

@domain_app.route('search/<string:id>')
def view_search(id):
    search = Search.query.filter_by(id=id).first()
    return render_template('index.html', domain_data=search.domain)