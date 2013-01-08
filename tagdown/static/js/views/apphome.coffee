define ['backbone', 'cs!models/doc', 'text!templates/doc.html'], 
	(Backbone, DocModels, doctmpl) ->
		DocList = DocModels.DocList
		DocView = Backbone.View.extend(
				'initialize': ->
					@render()
				,'render': ->
					el = DocView._tmpl(@model.toJSON())
					@setElement( el )
					return @$el
			,
				'_tmpl': _.template( doctmpl, null,
					'variable':'doc'
				)
		)
		AppHomeView = Backbone.View.extend 
			'name': 'AppHomeView'
			,'docs': null
			,'initialize': ->
				self = this
				@docs = new DocList()
				@docs.on('add', ->
					console.log("add")
				).on('change', ->
					console.log("change")
				).on('sync', (model, collection, options) ->
					for doc in model.models
						self.renderDoc(doc)
				)
				@docs.fetch()
			,'onAdd' : (model, collection, options) ->
				console.log(model)
			,'renderDoc' : (doc) ->
				docview = new DocView(model: doc)
				@$el.append(docview.$el)
				
			
				
				