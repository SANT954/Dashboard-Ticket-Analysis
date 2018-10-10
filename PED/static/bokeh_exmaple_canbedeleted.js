function execute(){ 

    var plt =  Bokeh.Plotting;
  const {Row} = Bokeh

    var pie_data = {
        labels: ['Work', 'Eat', 'Commute', 'Sport', 'Watch TV', 'Sleep'],
        values: [8, 2, 2, 4, 0, 8],
    };
 
	 var p0 = Bokeh.Charts.pie(pie_data,{outer_radius:0.5,
        inner_radius: 0.0,width:50,height:50,
        start_angle: Math.PI / 2,
        end_angle: 5 * Math.PI / 2,        toolbar_location:"",
    });
 
	 
	 plt.
	 
	var fig =plt.figure(p0)
   plt.show(fig, '#bokeh_ch1');

 
 }