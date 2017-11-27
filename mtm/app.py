import logging.config

from flask import Flask, Blueprint
from mtm import settings
from flask_cors import CORS, cross_origin
from mtm.api.songs.endpoint import ns as songsNamespace
from mtm.api.charts.endpoint import ns as chartsNamespace
from mtm.api.restplus import api
from mtm.models import db

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}) # enable cross-origin resource sharing
logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)


def configureApp():
    """
    Configures the application using the information from the settings
    """
    app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initializeApp():
    configureApp()

    # Creates blueprint for the API
    blueprint = Blueprint('api', __name__, url_prefix='/api')

    api.init_app(blueprint)
    api.add_namespace(songsNamespace)
    api.add_namespace(chartsNamespace)

    app.register_blueprint(blueprint)

    # Init app!
    db.init_app(app)


def main():
    initializeApp()
    log.info('>>>>> Starting development server at http://' + format(app.config['SERVER_NAME'] + '/api/ <<<<<'))
    app.run(debug = settings.FLASK_DEBUG)

if __name__ == "__main__":
    main()
