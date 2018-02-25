
import requests
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
from PED.data_layer import incident_sr_count
# Create your views here.

 
 
con = data_layer.getConnectionCursor()
cur=con.cursor()
     
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
    if request.method == 'GET':
        return JsonResponse({"script": "Ticket Details Will Appear Here"})
        # create a form instance and populate it with data from the request:
        
        # report_type': ['Ticket Report'
       
            # process the data in form.cleaned_data as required
            # ...HttpResponseRedirect('/' +data+'/')
            # redirect to a new URL:'/PED_summary/',

            # render(request, 'index.html', {'form': form,'asdf':data})
            
#         t = get_template('index.html')
#         html = t.render({'script': script,'div':div})
#         return HttpResponse(html)    
#         
       # return render(request, 'index.html', {'script': script,'div':div})
        #return JsonResponse({"script": "script"})
 
def pullQuickStats(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if request.POST.get('pullQuickStats') =='Yes':
            
            cur.execute(data_layer.current_open_count ) 
            current_open_count = cur.fetchall()
            
            cur.execute(data_layer.current_open_incidents ) 
            current_open_incidents= cur.fetchall()
            
            cur.execute(data_layer.current_open_srs) 
            current_open_srs= cur.fetchall()
            
            cur.execute(data_layer.current_open_auto_incidents) 
            current_open_auto_incidents = cur.fetchall()
            
            cur.execute(data_layer.current_open_manual_incidents) 
            current_open_manual_incidents= cur.fetchall()
            
            cur.execute(data_layer.current_open_p1s) 
            current_open_p1s= cur.fetchall()
            
            
            cur.execute(data_layer.current_open_aged_7) 
            current_open_aged_7= cur.fetchall()
        
            cur.execute(data_layer.current_open_aged_30) 
            current_open_aged_30= cur.fetchall()
                
                
            days_to_search=request.POST.get('days_to_search')
            if days_to_search=='Aged Between 7 and 30':
                cur.execute(data_layer.ticketicket_data_7) 
                ticketicket_data_ = cur.fetchall()
            
            elif days_to_search== 'Aged Beyond 30':     
                cur.execute(data_layer.ticketicket_data_30) 
                ticketicket_data_ = cur.fetchall()
            
             
                
    
    
            return JsonResponse({"current_open_count":current_open_count ,"current_open_incidents":current_open_incidents ,
                                 "current_open_srs":current_open_srs ,"current_open_auto_incidents":current_open_auto_incidents ,
                                 "current_open_manual_incidents":current_open_manual_incidents ,"current_open_p1s":current_open_p1s ,
                                 "current_open_aged_7":current_open_aged_7 ,"current_open_aged_30":current_open_aged_30 ,
                                 "ticketicket_data_": ticketicket_data_})


def pullLatestData(request):
    sync_job_status=''
    
    current_date="''"
        
    try:
        
        url='https://oihap.oraclecorp.com/osbcommon/TicketingService/TicketingRest/reports?id=103784&system=oal%20osvc'
        response = requests.get(url)
        response.encoding = 'utf-8'
        jsonResponse= response.json()
        
        jsonData = jsonResponse["report"]
        column=jsonData[0].get('columns')
        data=jsonData[0].get('rows')
        dat=data
        print(len(dat))
        cur.execute(data_layer.truncate_table)
        for rec in dat:
            '''name = item.get("rows")
            campaignID = item.get("lookupName")
            print(name)
            print(campaignID)'''
            item=rec.split(',')
             
            #print(item)
            if len(item[11])==0:
                item[11]="''"
                
            cur.execute("INSERT INTO REPORT ( TICKET, QUEUE, PRODUCT_ID, SOURCE_SYSTEM, CATEGORY, DISPOSITION, CONTROL_NUMBER, BUG_NUMBER, SEVERITY, STATUS,CREATED, CLOSED, ASSIGNED, UPDATED,  PRODUCT_HIERARCHY,  CREATED_BY ) VALUES ('"
            + str(item[0]) + '\',\'' +  str(item[1])+ '\',\'' 
            + str(item[2]) + '\',\'' +  str(item[3])+ '\',\''
            + str(item[4]) + '\',\'' +  str(item[5])+ '\',\''  
            + str(item[6]) + '\',\'' +  str(item[7])+ '\',\''  
            + str(item[8]) + '\',\'' +  str(item[9])+ '\','  
            #+ item[10] + '\',\'' +  item[11]+ '\',\''  
            + "to_date("  +  str(item[10])  +",'yyyy-mm-dd hh24:mi:ss')" +','
            + "to_date("  +  str(item[11])  +",'yyyy-mm-dd hh24:mi:ss')"+  ',\'' 
            + str(item[12]) + '\',' 
            + "to_date("  +  str(item[13])  +",'yyyy-mm-dd hh24:mi:ss')"+  ',\''  
            + str(item[14]) + '\',\''  
           # + "q\"[" +item[15] + "]\""+ '\',\'' +  str(item[16])+  "')")
            +  str(item[15])+  "')")
            con.commit()
        
        print("executed")
            
            
        
    except Exception as e :
        print(e) 
        sync_job_status='Error'
        current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        
        
    else: 
        sync_job_status='Success'
        current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        
        
        
    finally :
        cur.execute("INSERT INTO sync_job_status (last_updated_status, last_updated) VALUES ('" + sync_job_status +"'," + "to_date('"  +  str(current_date)  +"','yyyy-mm-dd hh24:mi:ss')"+ ")")
        con.commit()                
    return JsonResponse({"sync_job_status":sync_job_status})        


def getTicketData(request):
    if request.method == 'POST':
        if request.POST.get('getTicketData') =='Yes':
            
            cur.execute(data_layer.ticketicket_data_report) 
            ticketicket_data_report = cur.fetchall()
            
            return JsonResponse({ "daily_ticket_inflow": ticketicket_data_report})




def getTicket_7_Data(request):
    if request.method == 'POST':
        if request.POST.get('getTicket_7_Data') =='Yes':
            
            cur=con.cursor();
            cur.execute(data_layer.ticketicket_data_7) 
            ticketicket_data_7 = cur.fetchall()
            
            #con.close()
            return JsonResponse({ "ticketicket_data_7": ticketicket_data_7})

            		
 
def Ajax_Test(request):
        if request.method == 'GET':
               
               return HttpResponse("Successful GET request!")  # Sending an success response
        elif request.method == 'POST':
               return HttpResponse("Successful POST request!")
           

def pie_data(request):
    
    if request.method == 'POST':
        x = request.POST.get('pie_data')
        if x == 'Yes':
            x
            
             
            cur.execute(data_layer.incident_sr_count)
            incident_sr_count = {}
            
            for result in cur:
                incident_sr_count.update({result[0]:result[1]})
              
            cur.execute(data_layer.ticket_status)
            ticket_status = {}
            
            for result in cur:
                ticket_status.update({result[0]:result[1]})
            
            cur.execute(data_layer.ticket_source)
            ticket_source = {}
            
            for result in cur:
                ticket_source.update({result[0]:result[1]})
            
            cur.execute(data_layer.open_tickets_by_queue)
            open_tickets_by_queue = {}
            
            for result in cur:
                open_tickets_by_queue.update({result[0]:result[1]})
            
            cur.execute(data_layer.open_sr_ticket_source)
            open_sr_ticket_source = {}
            
            for result in cur:
                open_sr_ticket_source.update({result[0]:result[1]})
            
            cur.execute(data_layer.open_incident_ticket_source)
            open_incident_ticket_source = {}
            
            for result in cur:
                open_incident_ticket_source.update({result[0]:result[1]})
            
            return JsonResponse({ "incident_sr_count":incident_sr_count,"ticket_status":ticket_status,
                                 "ticket_source":ticket_source,"open_tickets_by_queue":open_tickets_by_queue,"open_sr_ticket_source":open_sr_ticket_source,
                                 "open_incident_ticket_source":open_incident_ticket_source
                                 
                                 })
           
 
def Incident_VS_SR(request):
    
    if request.method == 'POST':
        x = request.POST.get('Incident_VS_SR')
        if x == 'Yes':
            try:
                     
                 
                '''Daily inflow ''' 
                cur.execute(data_layer.daily_ticket_inflow)
                daily_ticket_inflow = cur.fetchall()
                
                '''Daily outflow'''
                cur.execute(data_layer.daily_ticket_outflow)
                daily_ticket_outflow = cur.fetchall()
                
                '''Weekly inflow''' 
                cur.execute(data_layer.weekly_ticket_inflow)
                weekly_ticket_inflow = cur.fetchall()
                
                '''Weekly outflow'''
                cur.execute(data_layer.weekly_ticket_outflow)
                weekly_ticket_outflow = cur.fetchall()
                  
            except:
                print("error occured")
            
            return JsonResponse({ "daily_ticket_inflow": daily_ticket_inflow, "daily_ticket_outflow": daily_ticket_outflow,
                                  "weekly_ticket_inflow": weekly_ticket_inflow, "weekly_ticket_outflow": weekly_ticket_outflow
                                 
                                 })
        
    
def InflowVSOutflow(request):
    
    if request.method == 'POST':
        x = request.POST.get('InflowVSOutflow')
        if x == 'Yes':
            try:
                     
                 
                '''Daily inflow ''' 
                cur.execute(data_layer.daily_ticket_inflow)
                daily_tick_inflow = cur.fetchall()
                
                daily_ticket_inflow = make_consistent(daily_tick_inflow)
                subset = daily_ticket_inflow[['Created', 'Incident_Count', 'SR_Count']]
                tuples_inflow = [tuple(x) for x in subset.values] 
                
                # daily_ticket_inflow['Created','Incident_Count','SR_Count']
                '''Daily outflow'''
                cur.execute(data_layer.daily_ticket_outflow)
                daily_tick_outflow = cur.fetchall()
                
                daily_ticket_outflow = make_consistent(daily_tick_outflow)
                # daily_ticket_outflow['Created','Incident_Count','SR_Count']
                subset_outflow = daily_ticket_inflow[['Created', 'Incident_Count', 'SR_Count']]
                tuples_outflow = [tuple(x) for x in subset_outflow.values]
                
                '''Weekly inflow''' 
                cur.execute(data_layer.weekly_ticket_inflow)
                weekly_ticket_inflow = cur.fetchall()
                
                '''Weekly outflow'''
                cur.execute(data_layer.weekly_ticket_outflow)
                weekly_ticket_outflow = cur.fetchall()
                  
            except Exception as e:
                print(e)
            
            return JsonResponse({ "daily_ticket_inflow":daily_tick_inflow, "daily_ticket_outflow":daily_tick_outflow,
                                  "weekly_ticket_inflow": weekly_ticket_inflow, "weekly_ticket_outflow": weekly_ticket_outflow
                                 
                                 })


def make_consistent(daily_ticket_inflow):
    daily_ticket_inflow_df = pd.DataFrame(daily_ticket_inflow, columns=['Created', 'Incident_Count', 'SR_Count'])
    print(daily_ticket_inflow_df.head(1))
    print(daily_ticket_inflow_df.dtypes)
    now = datetime.datetime.now()
    sysdate = now.strftime("%Y%m%d")
    daily_ticket_inflow_df['Created'] = pd.to_datetime(daily_ticket_inflow_df['Created'])
    print(daily_ticket_inflow_df.dtypes)
    dates_df = pd.DataFrame({'Created':pd.date_range('20170324', sysdate)}) 
    print(dates_df.head(1))
    # dates_df.loc['Incident_Count']=daily_ticket_inflow.['Incident_Count'] 
    # new_df=pd.merge(dates_df,daily_ticket_inflow_df,how='left',on='Created')
    return pd.merge(dates_df, daily_ticket_inflow_df, on='Created', how='outer')

    # new_df.to_csv(r"D:\PE report\new.csv")
    