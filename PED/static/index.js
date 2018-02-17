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
 * $(function fillData() { $('#table').bootstrapTable({ data: data });
 */

/*
 * function fillData() { console.log("asdfasdf");
 * 
 * $.ajax({ type : "POST", url : "/pull_data/", data : { id_select_Sprint :
 * $('#id_select_Sprint').val(), pulldata : 'Yes' },
 * 
 * success : function(data) { $('#table').bootstrapTable({ data: data } }) } }
 */


 

function getLatestData() {
	console.log("asdfasdf");

	$.ajax({
		type : "POST",
		url : "/pullLatestData/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			pulldata : 'Yes'
		},

		success : function(data) {
			console.log("asdfasdf");
			disableAllElements()
			$('#Sync_Job_Status').html(data.sync_job_status);
 
		}
	})
}

function disableAllElements() {
	document.getElementById("container1").style.display = 'none';
	document.getElementById("container2").style.display = 'none';
	document.getElementById("container3").style.display = 'none';
	document.getElementById("container4").style.display = 'none';
	document.getElementById("container5").style.display = 'none';
	document.getElementById("container6").style.display = 'none';
	document.getElementById("pie_container1").style.display = 'none';
	document.getElementById("pie_container2").style.display = 'none';
	document.getElementById("pie_container3").style.display = 'none';
	document.getElementById("pie_container4").style.display = 'none';
	document.getElementById("pie_container5").style.display = 'none';
	document.getElementById("pie_container6").style.display = 'none';
	document.getElementById("table-container").style.display = 'none';
}


 


function getTicketData() {
	console.log("asdfasdf");
	disableAllElements();
	document.getElementById("table-container").style.display = 'block';

	$.ajax({
		type : "POST",
		url : "/getTicketData/",
		"dataSrc" : "",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			getTicketData : 'Yes'
		},

		success : function(data) {

			/*
			 * $('#ticket_table').bootstrapTable({ data:
			 * [data.daily_ticket_inflow] })
			 */

			$(document).ready(function() {
				
			var	oTable=	$('#ticket_table').DataTable({
					data : data.daily_ticket_inflow,
					 paging: true,
					    searching: true,
					    destroy: true,
					   /* $(".dataTables_length select").addClass("selectpicker sel_id"),*/


					columns : [ {
						title : "TICKET"
					}, {
						title : "CATEGORY"
					}, {
						title : "DISPOSITION"
					}, {
						title : "CONTROL_NUMBE"
					}, {
						title : "BUG_NUMBER"
					}, {
						title : "STATUS"
					}, {
						title : "CREATED"
					}, {
						title : "ASSIGNED"
					} ]
				});
				
			onhover()
				  oTable.$('tr').tooltip( {
				        "delay": 0,
				        "track": true,
				        "fade": 250
				    } );
				
			});

		}
	})
}




function onhover(){
	
	$("#ticket_table  tbody tr").on('mouseover',function () {
		var thText = $(this).text();
		var hoverTxt;
		$.ajax({
		url : "/sprint_summary_post_form",
		async : false,
		success : function(respText) {
		hoverTxt = respText;
		}
		});
		this.setAttribute( 'title', hoverTxt.script );
		});
	/*
$('#ticket_table tbody tr').each( function() {	
    var sTitle;
    var nTds = $('td', this);
    var ticket_num = $(nTds[0]).text();

    $.ajax({
		type : "POST",
		url : "/sprint_summary_post_form/",
	    data: "ASDF",

		success : function(data) {
			console.log(data)
        sTitle = data.script;
		}
    
              } )
              this.setAttribute( 'title', data.script );
*/	
	
    
        
    
	  }




function pie_data() {

	disableAllElements()

	/*
	 * document.getElementById("container1").style.display = 'none';
	 * document.getElementById("container2").style.display = 'none';
	 * document.getElementById("container3").style.display = 'none';
	 * document.getElementById("container4").style.display = 'none';
	 * document.getElementById("container5").style.display = 'none';
	 * document.getElementById("container6").style.display = 'none';
	 */
	document.getElementById("pie_container1").style.display = 'block';
	document.getElementById("pie_container2").style.display = 'block';
	document.getElementById("pie_container3").style.display = 'block';
	document.getElementById("pie_container4").style.display = 'block';
	document.getElementById("pie_container5").style.display = 'block';
	document.getElementById("pie_container6").style.display = 'block';

	$
			.ajax({
				type : "POST",
				url : "/pie_data/",
				data : {
					id_select_Sprint : $('#id_select_Sprint').val(),
					pie_data : 'Yes'
				},

				success : function(data) {

					/*
					 * console.log(data["pie_dat"])
					 * console.log(data.pie_dat['Incident'])
					 * console.log(data["pie_dat"]['Service Request'])
					 * console.log(data["pie_dat"]['Incident'])
					 */

					incident_sr_count = data.incident_sr_count;
					ticket_status = data.ticket_status;
					ticket_source = data.ticket_source;
					open_tickets_by_queue = data.open_tickets_by_queue;
					open_sr_ticket_source = data.open_sr_ticket_source;
					open_incident_ticket_source = data.open_incident_ticket_source;

					var isc = [];
					for (i in incident_sr_count) {
						isc.push({
							"name" : i,
							"y" : incident_sr_count[i]
						});
					}

					var tstatus = [];
					for (i in ticket_status) {
						tstatus.push({
							"name" : i,
							"y" : ticket_status[i]
						});
					}

					var ts = [];
					for (i in ticket_source) {
						ts.push({
							"name" : i,
							"y" : ticket_source[i]
						});
					}

					var otq = [];
					for (i in open_tickets_by_queue) {
						otq.push({
							"name" : i,
							"y" : open_tickets_by_queue[i]
						});
					}

					var oss = [];
					for (i in open_sr_ticket_source) {
						oss.push({
							"name" : i,
							"y" : open_sr_ticket_source[i]
						});
					}

					var ois = [];
					for (i in open_incident_ticket_source) {
						ois.push({
							"name" : i,
							"y" : open_incident_ticket_source[i]
						});
					}

					draw_pie(isc, 'pie_container1', "Incident vs SR Count");
					draw_pie(tstatus, 'pie_container2',
							"Current Open Tickets By Status");
					draw_pie(ts, 'pie_container3',
							'Current Open Tickets By Source');
					draw_pie(otq, 'pie_container4',
							'Current Open Tickets By Queue');

					draw_pie(oss, 'pie_container5', 'Current Open SR By Source');
					draw_pie(ois, 'pie_container6',
							'Current Open Incidents By Source');
					/*
					 * draw_pie(dat,'pie_container7');
					 * draw_pie(dat,'pie_container8');
					 * 
					 * 
					 * draw_pie(dat,'pie_container9');
					 * draw_pie(dat,'pie_container10');
					 * draw_pie(dat,'pie_container11');
					 * draw_pie(dat,'pie_container12');
					 */
				}
			})
}

function Draw_InflowVSOutflow() {

	disableAllElements();
	
	document.getElementById("container1").style.display = 'block';
	document.getElementById("container2").style.display = 'block';
	document.getElementById("container3").style.display = 'block';
	document.getElementById("container4").style.display = 'block';
	/*document.getElementById("container5").style.display = 'none';
	document.getElementById("container6").style.display = 'none';
*/
 
	$.ajax({
		type : "POST",
		url : "/InflowVSOutflow/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			InflowVSOutflow : 'Yes'
		},

		success : function(data) {
			console.log('asdf')

			InflowVSOutflow(data.daily_ticket_inflow,
					data.daily_ticket_outflow, 'Daily ' + 'Incident '
							+ 'Inflow vs Outflow', 'Incident', 'container1');

			InflowVSOutflow(data.daily_ticket_inflow,
					data.daily_ticket_outflow, 'Daily ' + 'SR '
							+ 'Inflow vs Outflow', 'SR', 'container2');

			InflowVSOutflow(data.weekly_ticket_inflow,
					data.weekly_ticket_outflow, 'Weekly ' + 'Incident '
							+ 'Inflow vs Outflow', 'Incident', 'container3');

			InflowVSOutflow(data.weekly_ticket_inflow,
					data.weekly_ticket_outflow, 'Weekly ' + 'SR '
							+ 'Inflow vs Outflow', 'SR', 'container4');

		}
	})
}
function Disable_elements() {

	document.getElementById("pie_container1").style.display = 'none';
	document.getElementById("pie_container2").style.display = 'none';
	document.getElementById("pie_container3").style.display = 'none';
	document.getElementById("pie_container4").style.display = 'none';
	document.getElementById("pie_container5").style.display = 'none';
	document.getElementById("pie_container6").style.display = 'none';

}
function Draw_Incident_VS_SR() {

	
	disableAllElements();
	/*document.getElementById("container1").style.display = 'none';
	document.getElementById("container2").style.display = 'none';
	*/document.getElementById("container3").style.display = 'block';
	document.getElementById("container4").style.display = 'block';
	document.getElementById("container5").style.display = 'block';
	document.getElementById("container6").style.display = 'block';

	Disable_elements();

	$.ajax({
		type : "POST",
		url : "/Incident_VS_SR/",
		data : {
			id_select_Sprint : $('#id_select_Sprint').val(),
			Incident_VS_SR : 'Yes'
		},

		success : function(data) {

			Incident_VS_SR(data.daily_ticket_inflow, 'Daily Ticket Inflow',
					'container3');
			Incident_VS_SR(data.daily_ticket_outflow, 'Daily Ticket Outflow',
					'container4');
			Incident_VS_SR(data.weekly_ticket_inflow, 'Weekly Ticket Inflow',
					'container5');
			Incident_VS_SR(data.weekly_ticket_outflow, 'Weekly Ticket Outflow',
					'container6');

		}
	})
}

function parseISOLocal(s) {
	var b = s.split('-');
	// datestring=String(parseInt(b[0])+1) + b[1] +b[2]
	datestring = b[0] + b[1] + b[2]
	return new Date(datestring);
}

function bokeh_pie() {

	document.getElementById('bokeh_ch1').innerHTML = "";
	document.getElementById('bokeh_ch2').innerHTML = "";

	var plt = Bokeh.Plotting;

	var inc_sr = {
		labels : [ 'asdf', 'Sr' ],
		values : [ 53, 65 ]

	};

	var p0 = Bokeh.Charts.pie(inc_sr, {
		palette : [ '#FF8C00', '#A0522D' ],
		inner_radius : 0.0,
		start_angle : Math.PI / 2,
		end_angle : 5 * Math.PI / 2
	});

	p0.document.getElementById('bk-root')

	document.getElementById('bokeh_ch1').innerHTML = plt.show(p0);
	document.getElementById('bokeh_ch2').innerHTML = plt.show(p0);

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

			// $(div).html(data["div"]);
			// $("head").append(data["script"]);

			// var bokeh_data = JSON.parse(data);
			$('#bokeh_graph1').html(data.div1);
			$('#bokeh_graph2').html(data.div2);
			$('#bokeh_graph3').html(data.div2);
			$("head").append(data.script);
			$("head").append(data.script);
			$("head").append(data.script);

			/*
			 * var x= data["div"]; var y = data["script"];
			 * 
			 * var html = $.parseHTML( data );
			 * 
			 * $("#bokeh_id").html(eval(html['bokeh_id']) ); console.trace()
			 * console.log("this is console");
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
