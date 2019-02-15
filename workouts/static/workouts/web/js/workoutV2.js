$(document).ready(function() {
	
	var ex_options = "";	




	$.ajax({
    	url: '/workouts/api/exercise',
    	type: 'GET',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	},
	dataType: 'json',
	complete: function(data, statusText, xhr) {
		exercises = JSON.parse(data.responseJSON);
		for (var i=0; i < exercises.length; i++){
			ex_options += "<option value = " + exercises[i]['pk'] + ">" + exercises[i]['fields']['exercise_nm'] + "</option>";
		}	
   					
	}

    });



	addButton = document.getElementById("addButton");

	addButton.onclick = function () {
		var table= document.getElementById("workoutTable");
		var row = table.insertRow(-1);
		row.className += "setRow";
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		var cell3 = row.insertCell(2);
		var cell4 = row.insertCell(3);
		cell1.className += "exercise";
		cell2.className += "tdReps";
		cell3.className += "tdWeight";
		cell4.className += "tdDelete";

		// Add some text to the new cells:
		cell1.innerHTML = "<select class='exSelect'><option value='blank'>--Select--</option>" + ex_options + "</select>";
		cell2.innerHTML = "<input type='text' class='form-control reps' placeholder='#'>";
                cell3.innerHTML = "<input type='text' class='form-control weight' placeholder='lbs'>";
		cell4.innerHTML ='<button class="deleteButton">Delete</button>';
	}





	saveWorkoutButton = document.getElementById("saveWorkout");
	saveWorkout.onclick = function() {
	//table = document.getElementById("workoutTable");
	rows = table.getElementsByClassName("setRow");	


		for (var j=0; j< rows.length; j++){
		ex_id= rows[j].getElementsByClassName("exSelect")[0].value;
		reps = rows[j].getElementsByClassName("reps")[0].value;
		weight = rows[j].getElementsByClassName("weight")[0].value;
		addSet( ex_id, reps, weight);
		}
	

		endSession();

			
	  }

  


	


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


function addSet(ex_id, reps, weight) {
	console.log("ex_id:"+ex_id+", reps:"+reps+", weight:"+weight);
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




function endSession() {
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



window.onbeforeunload = function () {
	
	table = document.getElementById("workoutTable");
	
	rows = table.getElementsByTagName("tr");
	
	for (var i=1; i<rows.length; i++){
		
		reps = rows[i].getElementsByClassName("reps")[0].value;
		
		var to_save = 'reps_'+i.toString(); 
		
	 localStorage.setItem(to_save, reps);
    
    
    
	}
}


window.onload = function () {
	
	table = document.getElementById("workoutTable");
	
	rows = table.getElementsByTagName("tr");
	
	for (var i=1; i<rows.length; i++){
		
		varName = 'reps_' + i;
	
    	rows[i].getElementsByClassName("reps")[0].value = localStorage.getItem(varName);
	}

};
