from django.shortcuts import   render

from django.views.generic import TemplateView

from .forms import srint_select_form
from .reports import InteractiveGraph
from django.http.response import HttpResponse
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
 
 
def Ajax_Test(request):
        if request.method == 'GET':
               
               return HttpResponse("Successful GET request!") # Sending an success response
        elif request.method=='POST':
               return HttpResponse("Successful POST request!")