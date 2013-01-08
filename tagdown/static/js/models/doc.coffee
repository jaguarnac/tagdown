define ['underscore','backbone', 'showdown'],
(_, Backbone, Showdown) ->
	
	Doc = Backbone.Model.extend
		'initialize': () ->
			@set('id', @getID())
			@set('html', @getHTML())
		'getID': () ->
			@get('_id').$oid
		'getHTML': () ->
			md = @get('md') or ''
			html = new Showdown.converter().makeHtml(md)
			return html
			
	DocList = Backbone.Collection.extend
		'url': 'rest/docs/'
		'model': Doc
		
	
	DocModels = 
		'Doc' : Doc
		'DocList': DocList
	