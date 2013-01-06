define ['backbone', 'cs!models/doc'], 
	(Backbone, DocModels) ->
		'use strict'
		console.log(DocModels)
		AppHomeView = Backbone.View.extend 
			'name': 'AppHomeView'