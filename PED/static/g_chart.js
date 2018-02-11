

function draw_pie(data,e){
Highcharts.chart(e, {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    
    

    //var object={'positive':94,'neutral':2,'negative':2};

	 
    series: [{
            name: 'Brands',
            data: data
    }]
    
    })};
    
    

    function parseISOLocal(s) {
    	  var b = s.split('-');
    	  //datestring=String(parseInt(b[0])+1) + b[1] +b[2]
    	  datestring=b[0] + b[1] +b[2]
    	  return new Date(datestring);
    	}


    
    
    function draw_line(line,e){
    	var  incident_data=[];
		for(var i in line){
			
			date_=parseISOLocal(line[i][0])
				incident_data.push({"name": date_,"y":line[i][1]});
			
			
		//	dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
		}
		var sr_data=[]
for(var i in line){
			
			date_=parseISOLocal(line[i][0])
				sr_data.push({"name": date_,"y":line[i][2]});
			
			
		//	dat.push({"name":Date.parse(line[i][0]),"y":line[i][1]});
		}
    	
    	
    Highcharts.chart(e, {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
         },
        
         chart: {
             zoomType: 'x'
         },
         title: {
             text: 'Incident and SR inflow Graph'
         },
         subtitle: {
             text: document.ontouchstart === undefined ?
                     'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
         },
         xAxis: {
             type: 'datetime'
         },
         yAxis: {
             title: {
                 text: 'Inflow Count'
             }
         },
         legend: {
             enabled: false
         },
        xAxis: {
                type: 'datetime'
            },

        //var object={'positive':94,'neutral':2,'negative':2};

    	 
        series: [{
                name: 'Incident',
                data: incident_data
        }
           ,{
                name: 'SR',
                data: sr_data
        }]
        
        })};