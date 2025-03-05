from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialised datebase
db = SQLAlchemy()

# Define entries model
class TimelineEntry(db.Model):
    __tablename__ = 'entries'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(60), nullable=False, index=True)
    year = db.Column(db.SmallInteger, nullable=False, index=True)
    content = db.Column(db.Text(16000), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
