$(document).ready(function() {
    updateExList();

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

function CreateSession(indiv_id, gym_id) {
    $.ajax({
        url: '/workouts/api/session',
	type: 'POST',
	data: {
	    csrfmiddlewaretoken: "{{ csrf_token }}",
	    individual_id: indiv_id,
            gym_id: gym_id
	},
	dataType: 'json',
	complete: function(data) {
            json = JSON.parse(data.responseJSON);
	    console.log(json[0]);
	    session_id = json[0]['pk']
	    url = "/workouts/session?sid="+session_id;
	    window.location.href = url;
	}

    });


}

