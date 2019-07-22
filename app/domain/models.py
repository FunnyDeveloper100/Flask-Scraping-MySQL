from app.db import db
from datetime import datetime


""" Domain database schema """
class Domain(db.Model):
    __tablename__ = 'domains_csv'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(256))
    first_seen = db.Column(db.Integer)
    last_seen = db.Column(db.Integer)
    etld = db.Column(db.String(256))
    time_date_imported = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, domain, first_seen, last_seen, etld):
        self.domain = domain
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.etld = etld

    def __repr__(self):
        return self.domain