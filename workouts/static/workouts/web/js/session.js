
function AddSet() {
	button = document.getElementById("addSetButton");
	button.disabled= true;
	
    exercise = document.getElementById("exercise_id");
    ex_id = exercise.value;
    console.log(ex_id);
    weight = document.getElementById('weight').value;
    reps = document.getElementById('reps').value;
    
    $.ajax({
    url: '/workouts/api/set',
    type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    exercise_id: ex_id,
     	    weight: weight,
	    reps: reps
    	    
	},
	dataType: 'json',
	complete: function(data) {
            console.log('set api post complete');
	    document.getElementById("weight").value = '';
	    document.getElementById("reps").value = '';
	    
	    button.disabled = false;
	}

    });
}

function EndSession() {
    $.ajax({
	url: '/workouts/api/session',
	type: 'PUT',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}"
		},
	dataType: 'json',
	complete: function(data) {
        console.log('workout completed');
        json = JSON.parse(data.responseJSON);
	    console.log(json[0]);
	    session_id = json[0]['pk']
	    url = '/workouts/session_summary/'+session_id;
	    window.location.href = url;
	}


    });

}


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
function AddSet() {
	button = document.getElementById("addSetButton");
	button.disabled= true;
	
    exercise = document.getElementById("exercise_id");
    ex_id = exercise.value;
    console.log(ex_id);
    weight = document.getElementById('weight').value;
    reps = document.getElementById('reps').value;
    
    $.ajax({
    url: '/workouts/api/set',
    type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    exercise_id: ex_id,
     	    weight: weight,
	    reps: reps
    	    
	},
	dataType: 'json',
	complete: function(data) {
            console.log('set api post complete');
	    document.getElementById("weight").value = '';
	    document.getElementById("reps").value = '';
	    
	    button.disabled = false;
	}

    });
}

function EndSession() {
    $.ajax({
	url: '/workouts/api/session',
	type: 'PUT',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}"
		},
	dataType: 'json',
	complete: function(data) {
        console.log('workout completed');
        json = JSON.parse(data.responseJSON);
	    console.log(json[0]);
	    session_id = json[0]['pk']
	    url = '/workouts/session_summary/'+session_id;
	    window.location.href = url;
	}


    });

}
