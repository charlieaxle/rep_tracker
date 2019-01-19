$(document).ready(function() {

	var editButtons = document.getElementsByClassName("editButton");


	for (var i=0; i<editButtons.length; i++) {

		var button = editButtons[i];
		
		button.onclick = function() {

			this.innerText = "Save";
			
			
			var row = this.closest('tr');
			var ex_id = row.id;

			var exNameTD = row.getElementsByClassName("exName")[0];
			
			ex_nm = exNameTD.innerText;

			

			exNameTD.innerHTML = "<input type='text' class='form-control exNameInput' placeholder='"+ex_nm+"'>"

			
			this.onclick = function() {saveExercise(ex_id)};  
			
		}



	}



});


function saveExercise(ex_id) {

	row = document.getElementById(ex_id);

	ex_id = row.id;

	ex_nm_input = row.getElementsByTagName("input")[0];

	ex_nm = ex_nm_input.value;

	

	$.ajax({
    url: '/workouts/api/exercise',
    type: 'PUT',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    ex_nm: ex_nm,
     	    ex_id: ex_id
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
		
	td = row.getElementsByTagName("td")[0];
        td.innerHTML = ex_nm;
	button = row.getElementsByTagName("button")[0];
        button.innerText = "Edit";
	button.onclick = function() {return false};
			
	}

    });



}