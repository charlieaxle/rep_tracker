$(document).ready(function() {

	var startButtons = document.getElementsByClassName("startButton");


	for (var i=0; i<startButtons.length; i++) {

		var button = startButtons[i];
		
		button.onclick = function() {

			
			
			var row = this.closest('tr');
			var program_id = row.id;
			
			this.onclick = function() {startProgram(program_id)};  
			
		}



	}


function startProgram(program_id) {

    var url = '/workouts/startProgram?program_id='+program_id;
    window.location.href = url

};


});


