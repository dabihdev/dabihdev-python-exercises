from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime as dt

# We initialize the db object, but don't link the app yet
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(dt.timezone.utc))

    def __repr__(self):
        return f'<Task {self.id}>'