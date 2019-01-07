var session_id=0;
$(document).ready(function() {
    session_id = decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent("sid").replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1")); 
});

function AddSet() {
    exercise = document.getElementById("exercise_id");
    ex_id = exercise.value;

    weight = document.getElementById('weight').value;
    reps = document.getElementById('reps').value;
    
    $.ajax({
    url: '/workouts/api/set',
    type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    exercise_id: ex_id,
            session_id: session_id,
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
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    session_id: session_id,
	},
	dataType: 'json',
	complete: function(data) {
            console.log('workout completed');
	    url = '/workouts/session_summary/'+session_id
	    window.location.href = url;
	}


    });

}
