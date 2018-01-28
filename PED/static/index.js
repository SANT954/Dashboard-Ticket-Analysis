function clearReports(e) {

	document.getElementById('image_box').src = "";
	document.getElementById('showing_for').innerHTML = ""

}

function showing_ForText(e) {

	var x = document.getElementById("id_select_Sprint").value;

	console.log(document.getElementById("id_select_Sprint").value);

	document.getElementById('showing_for').innerHTML = "Showing " + e.value
			+ " for " + x;

}

function generateReport(e) {

	var x = document.getElementById("id_sprint").value;

	console.log(document.getElementById("id_sprint").value);
	if (x !== "Select Sprint") {
		document.getElementById('showing_for').innerHTML = "Showing " + e.value
				+ " for " + x;

		document.getElementById('image_box').src = "/media/" + x + "/" + e.id
				+ ".png";

	} else {

		document.getElementById('image_box').src = "";
		document.getElementById('showing_for').innerHTML = ""

	}
}

function loadDoc() {
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			document.getElementById("showing_for").innerHTML = this.responseText;
		}
	};
	xhttp.open("POST", "/media/", true);
	xhttp.send();
}

function doSomething() {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/media/",
		success : function(data) {

			$('#showing_for').html(data);
		}
	})
}

function doPOST() {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/media/",
		data : {
			post_id : 'catid'
		},

		success : function(data) {

			$('#showing_for').html(data);
		}
	})
}

function doPOSTForm(e) {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/sprint_summary_post_form/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			report_type : $(e).val()
		},

		success : function(data) {

			//$(div).html(data["div"]);
			//$("head").append(data["script"]);
 
			
			//var bokeh_data = JSON.parse(data);
		      $('#bokeh_graph').html(data.div);
		      $("head").append(data.script);

			
			
/*			var x= data["div"];
			var y = data["script"];
			
			 var html = $.parseHTML( data );

			$("#bokeh_id").html(eval(html['bokeh_id']) );
			console.trace()
			console.log("this is console");
*/			
			 
		}
	})
}

// CSRF code
function getCookie(name) {
	var cookieValue = null;
	var i = 0;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (i; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie
						.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// these HTTP methods do not require CSRF protection
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
	crossDomain : false, // obviates need for sameOrigin test
	beforeSend : function(xhr, settings) {
		if (!csrfSafeMethod(settings.type)) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
