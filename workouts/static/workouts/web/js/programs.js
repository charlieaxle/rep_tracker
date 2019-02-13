$(document).ready(function() {

	var startButtons = document.getElementsByClassName("startButton");


	for (var i=0; i<startButtons.length; i++) {

		var button = startButtons[i];
		
		button.onclick = function() {

			CreateSession();	
			
			var row = this.closest('tr');
			var program_id = row.id;
			startProgram(program_id);
		
			
		}



	}


function startProgram(program_id) {

    var url = '/workouts/startProgram?program_id='+program_id;
    window.location.href = url

};


});

function CreateSession() {
    	//link = document.getElementById("freeSessionButton");
	 // link.onclick = function() {return false;}
    

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
	}

    });

}

