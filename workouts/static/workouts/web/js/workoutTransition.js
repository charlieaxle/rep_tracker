$(document).ready(function() {
	
	freeWorkout = document.getElementById("freeSessionButton");

	//freeWorkout 




});





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



function CreateSession() {
    	link = document.getElementById("freeSessionButton");
	  link.onclick = function() {return false;}
    

    $.ajax({
        url: '/workouts/api/session',
	type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
            gym_id: 1
	},
	dataType: 'json',

	error: function(xhr, status, error) {
		element = document.getElementById("validationMessage");
		element.innerHTML = "<p>"+xhr.responseText+"</p>";
		},

	complete: function(data) {
            json = JSON.parse(data.responseJSON);
	    console.log(json[0]);
	    session_id = json[0]['pk'];
	    url = "/workouts/startProgram";
	    window.location.href = url;
	}

    });


}

