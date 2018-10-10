import datetime
from django.shortcuts import   render
from django.template.loader import get_template
import pandas as pd
from django.views.generic import TemplateView

from .forms import srint_select_form
from .reports import InteractiveGraph
from django.http.response import HttpResponse, JsonResponse
from PED import data_layer
from cx_Oracle import Connection as con
# Create your views here.
 
class PED_summary(TemplateView):

    def get(self, request, **kwargs):
        form = srint_select_form(initial={'18.2': '18.2'})
        return render(request, 'index.html', {'form':form})



		
		
def Fetch_Sprint(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = srint_select_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
             if 'Ticket Report' in request.POST:
                 script, div = InteractiveGraph().genTicketReport()
             elif 'Bug Report' in request.POST:
                 script, div = InteractiveGraph().genTicketReport()
			
            # process the data in form.cleaned_data as required
            # ...HttpResponseRedirect('/' +data+'/')
            # redirect to a new URL:'/PED_summary/',

			# render(request, 'index.html', {'form': form,'asdf':data})
	    
             return render(request, 'index.html', {'form':form, 'script' : script , 'div' : div})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = srint_select_form()

    return render(request, 'about.html', {'form': form})
 
        

def POSTForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        #report_type': ['Ticket Report'
        x = request.POST.get('report_type')
        if x=='Ticket Report':
            script, div = InteractiveGraph().genTicketReport()
        elif x=='Bug Report':
            script, div = InteractiveGraph().genTicketReport()
            
            # process the data in form.cleaned_data as required
            # ...HttpResponseRedirect('/' +data+'/')
            # redirect to a new URL:'/PED_summary/',

            # render(request, 'index.html', {'form': form,'asdf':data})
            
#         t = get_template('index.html')
#         html = t.render({'script': script,'div':div})
#         return HttpResponse(html)    
#         
       # return render(request, 'index.html', {'script': script,'div':div})
        return JsonResponse({"script": script, "div1": div,"div2": div,"div3": div})

		
 

def DataPull(request):
    
    if request.method == 'POST':
        x = request.POST.get('pulldata')
        if x=='Yes':
            return JsonResponse({"name": "santosh", "stargazers_count": "asdfa", "forks_count": "asdfa", "description": "asdfa"})
		
 
def Ajax_Test(request):
        if request.method == 'GET':
               
               return HttpResponse("Successful GET request!") # Sending an success response
        elif request.method=='POST':
               return HttpResponse("Successful POST request!")
           
           

def pie_data(request):
 
    
    
    if request.method == 'POST':
        x = request.POST.get('pie_data')
        if x=='Yes':
            x
            cur=data_layer.getConnectionCursor()
             
            cur.execute(data_layer.incident_sr_count)
            dic ={}
            
            for result in cur:
                dic.update({result[0]:result[1]})
              
            
            
            return JsonResponse({ "pie_dat": dic})
        
           
           
           
           
 
def Incident_VS_SR(request):
 
    
    
    if request.method == 'POST':
        x = request.POST.get('Incident_VS_SR')
        if x=='Yes':
            try:
                     
                cur=data_layer.getConnectionCursor()
                
                '''Daily inflow ''' 
                cur.execute(data_layer.daily_ticket_inflow)
                daily_ticket_inflow = cur.fetchall()
                
                '''Daily outflow'''
                cur.execute(data_layer.daily_ticket_outflow)
                daily_ticket_outflow= cur.fetchall()
                
                '''Weekly inflow''' 
                cur.execute(data_layer.weekly_ticket_inflow)
                weekly_ticket_inflow= cur.fetchall()
                
                '''Weekly outflow'''
                cur.execute(data_layer.weekly_ticket_outflow)
                weekly_ticket_outflow= cur.fetchall()
                
                  
            except:
                print("error occured")
            
            return JsonResponse({ "daily_ticket_inflow": daily_ticket_inflow,"daily_ticket_outflow": daily_ticket_outflow,
                                  "weekly_ticket_inflow": weekly_ticket_inflow,"weekly_ticket_outflow": weekly_ticket_outflow
                                 
                                 })
        
    
def InflowVSOutflow(request):
 
    
    
    if request.method == 'POST':
        x = request.POST.get('InflowVSOutflow')
        if x=='Yes':
            try:
                     
                cur=data_layer.getConnectionCursor()
                
                '''Daily inflow ''' 
                cur.execute(data_layer.daily_ticket_inflow)
                daily_tick_inflow = cur.fetchall()
                
                daily_ticket_inflow=make_consistent(daily_tick_inflow)
                subset = daily_ticket_inflow[['Created','Incident_Count','SR_Count']]
                tuples_inflow = [tuple(x) for x in subset.values] 

                
                #daily_ticket_inflow['Created','Incident_Count','SR_Count']
                '''Daily outflow'''
                cur.execute(data_layer.daily_ticket_outflow)
                daily_tick_outflow= cur.fetchall()
                
                daily_ticket_outflow=make_consistent(daily_tick_outflow)
                #daily_ticket_outflow['Created','Incident_Count','SR_Count']
                subset_outflow = daily_ticket_inflow[['Created','Incident_Count','SR_Count']]
                tuples_outflow = [tuple(x) for x in subset_outflow.values]
                
                '''Weekly inflow''' 
                cur.execute(data_layer.weekly_ticket_inflow)
                weekly_ticket_inflow= cur.fetchall()
                
                '''Weekly outflow'''
                cur.execute(data_layer.weekly_ticket_outflow)
                weekly_ticket_outflow= cur.fetchall()
                
                  
            except Exception as e:
                print(e)
            
            return JsonResponse({ "daily_ticket_inflow":daily_tick_inflow,"daily_ticket_outflow":daily_tick_outflow,
                                  "weekly_ticket_inflow": weekly_ticket_inflow,"weekly_ticket_outflow": weekly_ticket_outflow
                                 
                                 })
        


def make_consistent(daily_ticket_inflow ):
    daily_ticket_inflow_df=pd.DataFrame(daily_ticket_inflow,columns=['Created','Incident_Count','SR_Count'])
    print(daily_ticket_inflow_df.head(1))
    print(daily_ticket_inflow_df.dtypes)
    now = datetime.datetime.now()
    sysdate=now.strftime("%Y%m%d")
    daily_ticket_inflow_df['Created'] = pd.to_datetime(daily_ticket_inflow_df['Created'])
    print(daily_ticket_inflow_df.dtypes)
    dates_df=pd.DataFrame({'Created':pd.date_range('20170324', sysdate)}) 
    print(dates_df.head(1))
    #dates_df.loc['Incident_Count']=daily_ticket_inflow.['Incident_Count'] 
    #new_df=pd.merge(dates_df,daily_ticket_inflow_df,how='left',on='Created')
    return pd.merge(dates_df, daily_ticket_inflow_df, on='Created', how='outer')


    #new_df.to_csv(r"D:\PE report\new.csv")
    
