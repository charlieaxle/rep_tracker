$(document).ready(function() {
    updateExList();
    indiv_id = decodeURIComponent(window.location.search.replace(new RegExp("^(?:.*[&\\?]" + encodeURIComponent("uid").replace(/[\.\+\*]/g, "\\$&") + "(?:\\=([^&]*))?)?.*$", "i"), "$1"));
    console.log(indiv_id);
});



function updateExList() {

    $.ajax({
        crossOrigin: true,
        url: '/workouts/exercise',
        type: 'GET',
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",
        },
        dataType: 'json',
        complete: function(data) {
            json = JSON.parse(data.responseJSON);
            var ihtml = "";
            for (var i = 0; i < json.length; i++) {
                name = json[i]['fields']['exercise_nm'];
                document.getElementById("exList").innerHTML = ihtml;
                ihtml = ihtml + "<li>";
                ihtml = ihtml + name;
                ihtml = ihtml + "</li>";
                document.getElementById("exList").innerHTML = ihtml;
            };
        }
    })

}

function CreateEx() {
    ex_nm = document.getElementById("exercise_nm").value;
    ex_type = document.getElementById("ex_type_cd").value;

    $.ajax({
        crossOrigin: true,
        url: '/workouts/exercise',
        type: 'POST',
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",
            exercise_nm: ex_nm,
            ex_type_cd: ex_type
        },
        dataType: 'json',
        complete: function(data) {

            updateExList();

        }
    })
};

function CreateSession() {
    	link = document.getElementById("startSessionButton");
	    link.onclick = function() {return false;}
    

    $.ajax({
        url: '/workouts/api/session',
	type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
            gym_id: 1
	},
	dataType: 'json',
	complete: function(data) {
            json = JSON.parse(data.responseJSON);
	    console.log(json[0]);
	    session_id = json[0]['pk'];
	    url = "/workouts/session";
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

