from datetime import datetime

from mtm.models import db

class Ranks(db.Model):
    """
    Rank object that access the datasource through SQLAlchemy
    For more information take a look at:
    http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
    """

    #songId = db.Column(db.String(255))
    songId = db.Column(db.String(255), db.ForeignKey('songs.id'), nullable=False)
    startDate = db.Column(db.Date)
    endDate = db.Column(db.Date, primary_key=True)
    rank = db.Column(db.Integer, primary_key=True)


    def __init__(self, songId, startDate, endDate, rank):
        self.songId = songId
        self.startDate = startDate
        self.endDate = endDate
        self.rank = rank

    def __repr__(self):
        return '<Rank ' + self.songId + ' ' + self.song.name + ' ' + self.startDate + ': ' + rank + '>'