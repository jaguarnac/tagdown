from pyramid.renderers import render_to_response

class AppView(object):
    '''
    AppView class
    base class for all application views
    '''
    def __init__(self, request):
        self.request = request
        self.db = request.db
        self.context = {}
    
    def render(self, template):
        '''
        Renders the template using self.context
        @param template: template to render
        '''
        return render_to_response(template, self.context, request=self.request)
    
    def jsonresponse(self, template):
        pass
    
    def update_context(self, dict_obj):
        '''
        Update the context used for rendering the template
        '''
        self.context.update(dict_obj)
