from flask_restplus import fields
from mtm.api.restplus import api

# Song object used in endpoint responses
songResponseModel = api.model('Song', {
    'id': fields.String(readOnly=True, description='Unique identifier of a song', example='1'),
    'name': fields.String(required=True, description='Name of the song', example='Bad Romance'),
    'artist': fields.String(required=True, description='Name of the artist', example='Lady Gaga'),
    'albumName': fields.String(required=True, description='Name of the album', example='The Fame Monster'),
    'albumRelease': fields.Date(required=True, description='Release date of the album', example='2017-01-01'),
    'duration': fields.Integer(required=True, description='Duration of the song (in seconds)', example=60),
    'image': fields.String(required=True, description='Image of the album', example='http://example.com/gaga/ladygaga.jpg'),
    'url': fields.String(required=True, description='External link of the song', example='http://example.com/gaga/badromance')
})

# Media object used in endpoint responses
mediaResponseModel = api.model('Media', {
    'mediaType': fields.String(required=True, description='Type of the media object (image or video)', example='image'),
    'url': fields.String(required=True, description='External link for the media object', example='http://example.com/famemonster.jpg'),
    'caption': fields.String(required=True, description='Title for the media object', example='Lady Gaga - Bad Romance'),
    'thumbnail': fields.String(required=True, description='Thumbnail image for the media object', example='http://example.com/famemonster100x100.jpg')
})

# Media object used in endpoint responses
rankingResponseModel = api.model('Rank', {
    'startDate': fields.Date(readOnly=True, description='Start date of the ranking object', example='2017-01-01'),
    'endDate': fields.Date(readOnly=True, description='End date of the ranking object', example='2017-01-01'),
    'rank': fields.Integer(required=True, description='Rank position', example=1)
})

# Response wrapper for single songs
singleSongResponseModel = api.inherit('Song response', {
    'data': fields.Nested(songResponseModel)
})

# Response wrapper for list of media objects
listOfMediaResponseModel = api.inherit('Media response', {
    'data': fields.List(fields.Nested(mediaResponseModel))
})

# Response wrapper for list of ranking objects
listOfRankingResponseModel = api.inherit('Ranking response', {
    'data': fields.List(fields.Nested(rankingResponseModel))
})
