define ['underscore','backbone'],
(_, Backbone) ->
	'use strict'
	
	Doc = Backbone.Model.extend
		'initialize': () ->
			@id = @getID()  
		'getID': () ->
			@get('_id').$oid
			
	DocList = Backbone.Collection.extend
		'url': 'rest/docs/'
		'model': Doc
		
	
	DocModels = 
		'Doc' : Doc
		'DocList': DocList
	