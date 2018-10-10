from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import os 
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components


class InteractiveGraph:

    def genBugReport(self):

        x = [1, 3, 5, 7, 9, 11, 13]
        y = [1, 2, 3, 4, 5, 6, 7]
        title = 'y = f(x)'
    
        plot = figure(title=title ,
            x_axis_label='X-Axis',
            y_axis_label='Y-Axis',
                        
            )
        #plot.css_classes({'sizing_mode':'scale_both'})
        plot_line=plot.line(x, y, legend='f(x)', line_width=2)
        
        #plot_line.
        # Store components
         
        script, div = components(plot)
        
        # Feed them to the Django template.
        return  script, div
            
    def genTicketReport(self):
        x = [1, 3, 5, 7, 9, 11, 13]
        y = [1, 2, 3, 4, 5, 6, 7]
        title = 'y = f(x)'
    
        plot = figure(title=title ,
            x_axis_label='X-Axis',
            y_axis_label='Y-Axis',
                toolbar_location=None,
                plot_width=400,
                 plot_height=400)
        #plot.sizing_mode = "stretch_both"
    
        #plot.css_classes({'sizing_mode':'scale_both'})
        plot_line=plot.line(x, y,  line_width=2)
        
        #plot_line.
        # Store components
         
        script, div = components(plot)
        
         
        # Feed them to the Django template.
        return  script, div
