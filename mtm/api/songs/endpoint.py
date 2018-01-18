import logging

from flask import request
from flask_restplus import Resource, abort, reqparse
from mtm.api.errors import InvalidInputError, NotFoundError
from mtm.api.restplus import api
from mtm.api.songs.serializers import (listOfMediaResponseModel,
                                       listOfRankingResponseModel,
                                       singleSongResponseModel)
from mtm.models.media import Media
from mtm.models.ranks import Ranks
from mtm.models.songs import Songs
from sqlalchemy.sql import func

log = logging.getLogger(__name__)

# Creates namespace songs/ for operations associated to songs
ns = api.namespace('songs', description='Operations related to songs')

@ns.route('/<id>')
@api.response(400, 'Invalid ID supplied')
@api.response(404, 'Song not found.')
class SongItem(Resource):

    @api.marshal_with(singleSongResponseModel)
    def get(self, id):
        """
        Find song by ID
        """
        song = Songs.query.filter(Songs.id == id).first()

        if song == None:
            raise NotFoundError('The song with ID ' + str(id) + ' is not in our collection.')
        
        return { 'data': song }


@ns.route('/<id>/media')
@api.response(400, 'Invalid ID supplied')
@api.response(404, 'Song not found.')
class SongMedia(Resource):

    @api.marshal_with(listOfMediaResponseModel)
    @api.param('n', 'Number of media objects to return', required=False, default=3, type=int, min=1, max=10)
    def get(self, id):
        """
        List of related media of a song
        """
        parser = reqparse.RequestParser()
        parser.add_argument('n', required=False)
        args = parser.parse_args()

        n = 3
        try:
            n = int(args['n'])
        except:
            if args['n'] != None:
                raise InvalidInputError('The parameter n has to be an integer.')

        if n < 1 or n > 10:
            raise InvalidInputError('The parameter n has to be between 1 and 10.')

        media = Media.query.filter(Media.songId == id).limit(n)
        
        return { 'data': media }


@ns.route('/<id>/ranks')
@api.response(400, 'Invalid ID supplied')
@api.response(404, 'Song not found.')
class SongRanking(Resource):

    @api.marshal_with(listOfRankingResponseModel)
    def get(self, id):
        """
        List of rankings of a song ordered by date
        """       
        # TODO: Implement
        raise InvalidInputError('Method not implemented.')     
        
        return { 'data': '' }

