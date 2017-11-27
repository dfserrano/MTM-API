from datetime import datetime

from mtm.models import db

class Media(db.Model):
    """
    Song object that access the datasource through SQLAlchemy
    For more information take a look at:
    http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
    """

    songId = db.Column(db.String(255), primary_key=True)
    mediaType = db.Column(db.String(255))
    url = db.Column(db.String(255), primary_key=True)
    caption = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))


    def __init__(self, songId, mediaType, url, caption, thumbnail):
        self.songId = songId
        self.mediaType = mediaType
        self.url = url
        self.caption = caption
        self.thumbnail = thumbnail

    def __repr__(self):
        return '<Media ' + self.url + '>'
