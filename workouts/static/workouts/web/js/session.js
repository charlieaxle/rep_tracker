
function AddSet() {
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
	    url = '/workouts/session_summary'
	    window.location.href = url;
	}


    });

}
