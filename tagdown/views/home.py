from tagdown.base.appview import AppView
from pyramid.view import view_config

class HomeView(AppView):
    
    def __init__(self, request):
        AppView.__init__(self, request)
    
    @view_config(route_name='home')
    def tdhome(self):
        docs = self.request.db['docs'].find()
        self.update_context(
            {
             'name':'Nachiket',
             'docs': docs
            }
        )
        return self.render('templates/home.jinja2')
    
    @view_config(route_name='form')
    def docform(self):
        post = self.request.POST
        doc = {}
        if post:
            tags_str = post.get('doc_tags')
            tags = [tag.strip() for tag in tags_str.split(',')]
            doc = {
                'title': post.get('doc_title'),
                'md': post.get('doc_md'),
                'tags': tags
            }
            doc_id = self.request.db['docs'].insert(doc)
            doc = self.request.db['docs'].find_one({'_id':doc_id})
            tags = doc.get('tags')
            tags_str = ', '.join(tags)
            doc['tags_str'] = tags_str
        self.update_context({'post':post, 'doc': doc})
        return self.render('templates/form.jinja2')