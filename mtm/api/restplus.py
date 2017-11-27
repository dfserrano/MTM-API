import logging
import traceback

from flask_restplus import Api
from mtm import settings
from mtm.api.errors import InvalidInputError, NotFoundError

log = logging.getLogger(__name__)

api = Api(version='1.0', title='The Music Time Machine API',
          description='The Music Time Machine is a test API created for CMPUT 401 at the University of Alberta.')

def getErrorObject(e):
    """
    Gets an error object to return in the response.
    @type  e: Exception
    @param e: The exception object.
    @rtype: dict
    @return: An error object
    """
    return {
        'errors': [{
            'code': e.code,
            'title': e.title,
            'details': e.details,
            'href': e.href
        }],
        'message': 'Some errors were found during the execution of this request'
    }

@api.errorhandler
def defaultErrorHandler(e):
    """
    Handles error responses for undefined exceptions.
    @type  e: Exception
    @param e: The exception object.
    """
    e.message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return getErrorObject(e), 500


@api.errorhandler(InvalidInputError)
def invalidInputErrorHandler(e):
    """
    Handles error responses for invalid input errors.
    @type  e: Exception
    @param e: The exception object.
    """
    return getErrorObject(e), 404


@api.errorhandler(NotFoundError)
def notFoundErrorHandler(e):
    """
    Handles error responses for not found errors.
    @type  e: Exception
    @param e: The exception object.
    """
    return getErrorObject(e), 404
