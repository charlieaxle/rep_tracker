function addExercise() {
	var exercise_nm = document.getElementById("exerciseName").value;
	var ex_type_id = document.getElementById("exercise_type_id").value;
	console.log(exercise_nm);
	console.log(ex_type_id);
	
	$.ajax({
    url: '/workouts/api/exercise',
    type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    exercise_nm: exercise_nm,
     	    ex_type_id: ex_type_id
	},
	dataType: 'json',
	error: function(xhr, status, error) {
		element = document.getElementById("validationMessage");
		element.innerHTML = "<p>"+xhr.responseText+"</p>";
	},
	complete: function(data, statusText, xhr) {
		console.log("STATUSTEXT: "+statusText);
	;	
        console.log('exercise api post complete');
	    document.getElementById("exerciseName").value = '';
	    document.getElementById("exercise_type_id").value = '0';
             url = "/workouts/userExercises"
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