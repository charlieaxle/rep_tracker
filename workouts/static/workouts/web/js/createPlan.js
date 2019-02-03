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
		var table= document.getElementById("programTable");
		var row = table.insertRow(-1);
		row.className += "setRow";
		var cell1 = row.insertCell(0);
		var cell2 = row.insertCell(1);
		var cell3 = row.insertCell(2);

		// Add some text to the new cells:
		cell1.innerHTML = "<select class='exSelect'><option value='blank'>--Select--</option>" + ex_options + "</select>";
		cell2.innerHTML = "<input type='text' class='form-control sets' placeholder='#'>";
		cell3.innerHTML ='<td><button class="deleteButton">Delete</button></td>';
	}


});


function saveProgram() {

	nameInput = document.getElementById("programName");
	programName= nameInput.value;
	
	$.ajax({
    	url: '/workouts/api/program',
    	type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    program_nm : programName
	},
	dataType: 'json',
	complete: function(data, statusText, xhr) {
		console.log('Program Added');	
		program = JSON.parse(data.responseJSON)[0] ;
		program_id = program['pk'];
		
		rows = document.getElementsByClassName("setRow");
		for (var j=0; j< rows.length; j++){
			ex_id= rows[j].getElementsByClassName("exSelect")[0].value;
			numSets = rows[j].getElementsByClassName("sets")[0].value;
			prog_order_nbr = j;
			addPlannedSet(ex_id, numSets, program_id, prog_order_nbr);
		}
		url = "/workouts/userPrograms"
	    window.location.href = url;

						
	}

    	});

};

function addPlannedSet(ex_id, numSets, program_id, prog_order_nbr) {

	$.ajax({
		url: '/workouts/api/plannedSets',
		type : 'POST',
		data: {
			csrfmiddlewaretoken: "{{ csrf_token }}",
			ex_id : ex_id,
			num_sets : numSets,
			program_id : program_id,
             		prog_order_nbr : prog_order_nbr
		},
		dataType : 'json',
		complete: function(data, statusText, xhr) {
			console.log("set(s) added");
		}

	});

};
