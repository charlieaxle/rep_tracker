function createUser() {
	console.log("test");
	user_name = document.getElementById("userNameInput").value;

	url = "/workouts/api/individual";
	
	$.ajax({
		url: url,
		type: 'POST',
		data: {
	    		csrfmiddlewaretoken: "{{ csrf_token }}",
			user_nm : user_name
		},

		dataType : 'json',
		complete: function(data) {
			console.log('User Created');
            		json = JSON.parse(data.responseJSON);
	    		console.log(json[0]);
	    		user_id = json[0]['pk']
	    		url = "/workouts/home?uid="+user_id;
	    		window.location.href = url;
			}


	})
}


function signInUser() {
	user_nm = document.getElementById("inputSignIn").value;
	console.log(user_nm);

		url = "/workouts/api/individual";
	
	$.ajax({
		url: url,
		type: 'GET',
		data: {
	    		csrfmiddlewaretoken: "{{ csrf_token }}",
			user_nm : user_nm
		},

		dataType : 'json',
		complete: function(data) {
			console.log('User Retrieved');
            		json = JSON.parse(data.responseJSON);
	    		console.log(json[0]);
	    		user_id = json[0]['pk']
	    		url = "/workouts/home?uid="+user_id;
	    		window.location.href = url;
			}


	})

}