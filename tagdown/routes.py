#routing file for the application
def make_routes(config):
    
    #routes & views
    config.add_route('home','/')
    config.add_route('form', '/docform/')
    config.add_route('docs', '/rest/docs/')
    config.add_route('doc', 'rest/docs/{id}')
    
    
    #static views
    config.add_static_view('static', 'tagdown:static')