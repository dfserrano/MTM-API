from datetime import datetime

from mtm.models import db

class Songs(db.Model):
    """
    Song object that access the datasource through SQLAlchemy
    For more information take a look at:
    http://flask-sqlalchemy.pocoo.org/2.3/quickstart/
    """

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    albumName = db.Column(db.String(255))
    albumRelease = db.Column(db.Date)
    duration = db.Column(db.Integer)
    image = db.Column(db.String(255))
    url = db.Column(db.String(255))

    ranks = db.relationship('Ranks', backref='song', lazy=True)

    def __init__(self, id, name, artist, albumName, albumRelease, duration, image, url):
        """
        Initializes a Song object.
        @type  name: string
        @param name: The ID of the song.
        @type  name: string
        @param name: The name of the song.
        @type  artist: string
        @param artist: The name of the artist.
        @type  albumName: string
        @param albumName: The name of the album.
        @type  albumRelease: number
        @param year: The release date of the album.
        @type  duration: number
        @param year: The duration of the song.
        @type  image: string
        @param image: The image of the album cover.
        @type  url: string
        @param url: The external link for the song.
        """
        self.id = id
        self.name = name
        self.artist = artist
        self.albumName = albumName
        self.albumRelease = albumRelease
        self.duration = duration
        self.image = image
        self.url = url

    def __repr__(self):
        return '<Song ' + self.name + ' - ' + self.artist + '>'
