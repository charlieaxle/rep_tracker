function signOutUser() {

    $.ajax({
        url: '/workouts/api/signOut',
	type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	},
	dataType: 'json',
	complete: function(data) {
         
	    console.log('logged out');
	    url = "/workouts"
	    window.location.href = url;
	  }

    });



}
