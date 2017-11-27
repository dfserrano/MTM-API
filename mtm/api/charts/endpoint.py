import logging

from flask import request
from flask_restplus import Resource, abort, reqparse
from mtm.api.errors import InvalidInputError, NotFoundError
from mtm.api.restplus import api
from mtm.api.charts.serializers import chartResponseModel
from mtm.models.ranks import Ranks
from mtm.models.songs import Songs
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import calendar

log = logging.getLogger(__name__)

# Creates namespace charts/ for operations associated to song charts
ns = api.namespace('charts', description='Operations related to charts')

@ns.route('/<date>')
@api.response(400, 'Invalid date supplied')
@api.response(404, 'Chart not found.')
class ChartItem(Resource):

    @api.marshal_with(chartResponseModel)
    def get(self, date):
        """
        Find chart by date
        """
        try:
            chartDate = datetime.strptime(date, "%Y-%m-%d") + timedelta(hours=-1)
        except ValueError:
            raise InvalidInputError('The parameter date is invalid (Expected format YYYY-mm-dd).')

        print(chartDate.time())
        print(calendar.timegm(chartDate.utctimetuple()))
        chart = Ranks.query.filter(Ranks.startDate <= chartDate, Ranks.endDate >= chartDate).order_by(Ranks.rank).limit(10)
        
        if chart == None:
            raise NotFoundError('The chart for the date ' + date + ' is not in our collection.')
        
        return { 'data': chart }