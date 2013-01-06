require.config({
	'paths':{
		'jquery': 'jquery-1.8.3'
	},
	'shim':{
		'underscore':{
			'exports': '_'
		},
		'backbone':{
			'deps': ['underscore', 'jquery'],
			'exports': 'Backbone'
		}
	}
})
require(
['cs!tagdown'], 
function() {
});