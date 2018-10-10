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



/* 
$(function fillData() {
    $('#table').bootstrapTable({
        data: data
    });
 */
	
/*	
function fillData() {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/pull_data/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			pulldata : 'Yes'
		},

		success : function(data) {
		      $('#table').bootstrapTable({
        data: data

		}
	})
}
}*/

function fillData() {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/pull_data/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			pulldata : 'Yes'
		},

		success : function(data) {
			console.log("asdfasdf");

			$('#table').bootstrapTable({
		          data: [data] })
 			 
		}
	})
}



function pie_data() {
 
    document.getElementById("container1").style.display='block';
    document.getElementById("container2").style.display='block';
    document.getElementById("container3").style.display='none';
    document.getElementById("container4").style.display='none';
    document.getElementById("container5").style.display='none';
    document.getElementById("container6").style.display='none';

    
    
    $.ajax({
		type : "POST",
		url : "/pie_data/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			pie_data : 'Yes'
		},

		success : function(data) {
			
			console.log(data["pie_dat"])
			console.log(data.pie_dat['Incident'])
 			console.log(data["pie_dat"]['Service Request'])
			console.log(data["pie_dat"]['Incident'])
			pie=data.pie_dat;
			var  dat=[];
			for(i in pie ){
				dat.push({"name":i,"y":pie[i]});
			}
			draw_pie(dat,'container1');
			draw_pie(dat,'container2');
		}
	})
}


function Draw_InflowVSOutflow() {
	 
    document.getElementById("container1").style.display='none';
    document.getElementById("container2").style.display='none';
    document.getElementById("container3").style.display='block';
    document.getElementById("container4").style.display='block';
    document.getElementById("container5").style.display='none';
    document.getElementById("container6").style.display='none';
    
    
	$.ajax({
		type : "POST",
		url : "/InflowVSOutflow/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			InflowVSOutflow : 'Yes'
		},

		success : function(data) {
			 console.log('asdf')
			 
			InflowVSOutflow(data.daily_ticket_inflow,data.daily_ticket_outflow,'Daily '+'Incident'+' Inflow vs Outflow','Incident','container3');

			 InflowVSOutflow(data.daily_ticket_inflow,data.daily_ticket_outflow,'Daily '+'SR'+' Inflow vs Outflow','SR','container4');
		}
	})
}

function Draw_Incident_VS_SR() {
	 
    document.getElementById("container1").style.display='none';
    document.getElementById("container2").style.display='none';
    document.getElementById("container3").style.display='block';
    document.getElementById("container4").style.display='block';
    document.getElementById("container5").style.display='block';
    document.getElementById("container6").style.display='block';
    
    
	$.ajax({
		type : "POST",
		url : "/Incident_VS_SR/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			Incident_VS_SR: 'Yes'
		},

		success : function(data) {
		 
			Incident_VS_SR(data.daily_ticket_inflow,'Daily Ticket Inflow','container3');
			Incident_VS_SR(data.daily_ticket_outflow,'Daily Ticket Outflow','container4');
			Incident_VS_SR(data.weekly_ticket_inflow,'Weekly Ticket Inflow','container5');
			Incident_VS_SR(data.weekly_ticket_outflow,'Weekly Ticket Outflow','container6');
		
		}
	})
}

function parseISOLocal(s) {
	  var b = s.split('-');
	  //datestring=String(parseInt(b[0])+1) + b[1] +b[2]
	  datestring=b[0] + b[1] +b[2]
	  return new Date(datestring);
	}


function bokeh_pie(){ 

	document.getElementById('bokeh_ch1').innerHTML=""; 
	document.getElementById('bokeh_ch2').innerHTML=""; 

	var plt =  Bokeh.Plotting;
 
	
	var inc_sr={labels:['asdf','Sr'],
		values: [53,65]
		
	};
	
	
	 var p0 = Bokeh.Charts.pie(inc_sr,{palette:['#FF8C00'	,'#A0522D'],
        inner_radius: 0.0,
        start_angle: Math.PI / 2,
        end_angle: 5 * Math.PI / 2
    });
    
	 p0.document.getElementById('bk-root')
	 
	 
    document.getElementById('bokeh_ch1').innerHTML=plt.show(p0);
    document.getElementById('bokeh_ch2').innerHTML=plt.show(p0);
	
	
	
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
		      $('#bokeh_graph1').html(data.div1);
		      $('#bokeh_graph2').html(data.div2);
		      $('#bokeh_graph3').html(data.div2);
		      $("head").append(data.script);
		      $("head").append(data.script);
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
