from flask_restplus import fields
from mtm.api.restplus import api

# Chart item object used in endpoint responses
chartItemResponseModel = api.model('ChartItem', {
    'rank': fields.Integer(required=True, description='Rank position of the song', example=1),
    'startDate': fields.Date(required=True, description='Rank position of the song'),
    'endDate': fields.Date(required=True, description='Rank position of the song'),
    'songId': fields.String(readOnly=True, description='Unique identifier of a song', example='1'),
    'song.name': fields.String(readOnly=True, description='Unique identifier of a song', example='Bad Romance'),
    'song.artist': fields.String(readOnly=True, description='Unique identifier of a song', example='Lady Gaga'),
})

# Response wrapper for list of chart item objects
chartResponseModel = api.inherit('Chart response', {
    'data': fields.List(fields.Nested(chartItemResponseModel))
})
