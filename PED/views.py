from django.shortcuts import   render
from django.template.loader import get_template

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
            con=data_layer.getConnection()
            cur = con.cursor()
            cur.execute(data_layer.incident_sr_count)
            dic ={}
            
            for result in cur:
                dic.update({result[0]:result[1]})
              
            
            
            return JsonResponse({ "pie_dat": dic})
        
           
           
           
           
 
def line_data(request):
 
    
    
    if request.method == 'POST':
        x = request.POST.get('line_data')
        if x=='Yes':
            try:
                    
                con=data_layer.getConnection()
                cur = con.cursor()
                cur.execute(data_layer.incident_sr_outflow)
                
                recs = cur.fetchall()
    
      
                  
            except:
                print("error occured")
            
            return JsonResponse({ "line_dat": recs})
        
                     