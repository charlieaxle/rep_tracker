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
	complete: function(data) {
            console.log('exercise api post complete');
	    document.getElementById("exerciseName").value = '';
	    document.getElementById("exercise_type_id").value = '0';
	}

    });
	
}