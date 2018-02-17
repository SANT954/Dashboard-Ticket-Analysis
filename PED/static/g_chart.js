
function draw_pie(data, e, title) {
	Highcharts
			.chart(
					e,
					{
						chart : {
							plotBackgroundColor : '#E3FFE3',
							plotBorderWidth : null,
							plotShadow : false,
							type : 'pie'
						},
						title : {
							text : title
						},
						credits : {
							enabled : false
						},
						exporting : {
							enabled : false
						},

						tooltip : {
							pointFormat : '{series.name}: <b>{point.percentage:.1f}%</b>'
						},
						plotOptions : {
							pie : {
								allowPointSelect : true,
								size : 200,

								cursor : 'pointer',
								dataLabels : {
									enabled : true,
									format : '<b>{point.name}</b>: {point.percentage:.1f} %',
									style : {
										color : (Highcharts.theme && Highcharts.theme.contrastTextColor)
												|| 'black'
									}
								}
							}
						},

						series : [ {
							name : 'Tickets',
							colorByPoint : true,
							data : data
						} ]

					})
};

function parseISOLocal(s) {
	var b = s.split('-');
	// datestring=String(parseInt(b[0])+1) + b[1] +b[2]
	datestring = b[0] + b[1] + b[2]
	return new Date(datestring);
}

function Incident_VS_SR(line, title, e) {
	var incident_data = [];
	for ( var i in line) {

		incident_date = parseISOLocal(line[i][0])
		incident_data.push([ Date.parse(line[i][0]), line[i][1] ]);

		// dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
	}
	var sr_data = []
	for ( var i in line) {

		sr_date = parseISOLocal(line[i][0])
		sr_data.push([ Date.parse(line[i][0]), line[i][2] ]);

		// dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
	}

	Highcharts
			.chart(
					e,
					{
						chart : {
							plotBackgroundColor : null,
							plotBorderWidth : null,
							plotShadow : false,
						},

						chart : {
							zoomType : 'x'
						},credits : {
							enabled : false
						},
						exporting : {
							enabled : false
						},
						title : {
							text : title
						},
						subtitle : {
							text : document.ontouchstart === undefined ? 'Click and drag in the plot area to zoom in'
									: 'Pinch the chart to zoom in'
						},
						xAxis : {
							type : 'datetime',
							labels : {
								format : '{value:%Y-%b-%e}'
							}
						},
						yAxis : {
							title : {
								text : 'Inflow Count'
							}
						},
						legend : {
							enabled : false
						},
						// var object={'positive':94,'neutral':2,'negative':2};

						series : [ {
							name : "Incident",
							data : incident_data
						}, {
							name : "SR",
							data : sr_data
						} ]

					})
};

function InflowVSOutflow(ticket_inflow, ticket_outflow, title, category, e) {

	if (category == 'Incident') {
		category_index = 1
	} else {
		category_index = 2
	}
	/*
	 * var inflow_data=[]; for(var i in ticket_inflow){
	 * 
	 * inflow_date=parseISOLocal(ticket_inflow[i][0]) inflow_data.push({"name":
	 * inflow_date,"y":ticket_inflow[i][category_index]});
	 * 
	 *  // dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]}); }
	 * 
	 * 
	 * 
	 * 
	 * 
	 */var inflow_data = [];
	for ( var i in ticket_inflow) {

		inflow_data.push([ Date.parse(ticket_inflow[i][0]),
				ticket_inflow[i][category_index] ]);

		// dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
	}

	var outflow_data = []
	for ( var i in ticket_outflow) {

		// outflow_date=parseISOLocal(ticket_outflow[i][0])
		outflow_data.push([ Date.parse(ticket_outflow[i][0]),
				ticket_outflow[i][category_index] ]);

		// dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
	}

	Highcharts
			.chart(
					e,
					{
						chart : {
							plotBackgroundColor : null,
							plotBorderWidth : null,
							plotShadow : false,
						},

						chart : {
							zoomType : 'x'
						},
						credits : {
							enabled : false
						},
						exporting : {
							enabled : false
						},
						title : {
							text : title
						},
						subtitle : {
							text : document.ontouchstart === undefined ? 'Click and drag in the plot area to zoom in'
									: 'Pinch the chart to zoom in'
						},
						xAxis : {
							type : 'datetime',
							labels : {
								format : '{value:%Y-%b-%e}'
							}
						},
						yAxis : {
							title : {
								text : 'Inflow Count'
							}
						},
						legend : {
							enabled : false
						},

						series : [ {
							name : 'Incident',
							data : inflow_data
						}, {
							name : 'Incident',
							data : outflow_data
						} ]

					})
};
