from tagdown.base.appview import AppView
from pyramid.view import view_config, view_defaults
from bson import json_util
from bson.objectid import ObjectId

@view_defaults(route_name='docs', renderer='mongojson')
class DocView(AppView):
    @view_config()
    def get(self):
        docs = [doc for doc in self.db['docs'].find()]
        return docs
    
    @view_config(route_name='doc')
    def get_one(self):
        docid = self.request.matchdict.get('id')
        doc = self.db['docs'].find_one({'_id': ObjectId(docid) })
        return doc
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass   