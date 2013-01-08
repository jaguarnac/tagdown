define ['jquery','cs!views/apphome'],
	($, AppHomeView)-> 
		app = new AppHomeView ( 
			el: $('#main')
		)