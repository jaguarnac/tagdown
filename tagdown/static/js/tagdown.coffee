define ['jquery','cs!views/apphome'],
	($, AppHomeView)-> 
		'use strict'
		console.log new AppHomeView ( 
			el: $('#main')
		)
