import uuid
from app.db import db
from datetime import datetime
from sqlalchemy.orm import relationship

results = db.Table('results',
                   db.Column('domain_id', db.Integer, db.ForeignKey(
                       'domains_csv.id'), primary_key=True),
                   db.Column('search_id', db.String(256),
                             db.ForeignKey('search.id'), primary_key=True)
                   )


class Domain(db.Model):
    __tablename__ = 'domains_csv'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(256))
    first_seen = db.Column(db.Integer)
    last_seen = db.Column(db.Integer)
    etld = db.Column(db.String(256))
    time_date_imported = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    search = db.relationship(
        'Search', secondary=results, back_populates='domain')

    def __init__(self, domain, first_seen, last_seen, etld):
        self.domain = domain
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.etld = etld

    def __repr__(self):
        return self.domain


def generate_uuid():
    return str(uuid.uuid4())


class Search(db.Model):
    __tablename__ = 'search'
    id = db.Column(db.String(256), primary_key=True, default=generate_uuid)
    keyword = db.Column(db.String(256))
    domain = db.relationship(
        'Domain', secondary=results, back_populates='search')

    def __init__(self, keyword):
        self.keyword = keyword

    def __repr__(self):
        self.keyword
