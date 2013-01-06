from pyramid.config import Configurator
from pyramid.events import subscriber
from pyramid.events import NewRequest
from routes import make_routes
import pymongo

from tagdown.resources import Root
from pyramid.renderers import JSON
from tagdown.base.renderers import mongo_json_serializer

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    config = Configurator(settings=settings, root_factory=Root)
    
    #add debug toolbar
    config.include('pyramid_debugtoolbar')
    
    #add jinja2 support
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path("tagdown:templates")
    
    #add a mongo-json renderer
    config.add_renderer('mongojson', JSON(serializer=mongo_json_serializer))
    
    #routes
    make_routes(config)
    
    # MongoDB
    def add_mongo_db(event):
        settings = event.request.registry.settings
        url = settings['mongodb.url']
        db_name = settings['mongodb.db_name']
        db = settings['mongodb_conn'][db_name]
        event.request.db = db
    db_uri = settings['mongodb.url']
    MongoDB = pymongo.Connection
    if 'pyramid_debugtoolbar' in set(settings.values()):
        class MongoDB(pymongo.Connection):
            def __html__(self):
                return 'MongoDB: <b>{}></b>'.format(self)
    conn = MongoDB(db_uri)
    config.registry.settings['mongodb_conn'] = conn
    config.add_subscriber(add_mongo_db, NewRequest)
    config.scan()
    return config.make_wsgi_app()
