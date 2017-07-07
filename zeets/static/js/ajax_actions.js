(function(){
	var jquery_version = '3.2.1';
	var site_url = 'http://127.0.0.1:8000/';
	var static_url = site_url + 'static/';
	var conflict = typeof window.$ != 'undefined';
	var script = document.createElement('script');
	script.setAttribute('src', 'jquery-3.2.1.min.js');
	document.getElementByTagName('head')[0].appendChild(script);
	var attempts = 15;
	(function(){
		if(typeof window.jQuery == 'undefined'){
			if(--attempts > 0){
				window.setTimeout(arguments.callee, 250)
			}else{
				alert('An error occurred while loading jQuery')
			}
		}
	})
})