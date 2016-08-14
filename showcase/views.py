from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Work
from .forms import WorkForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
def index(request):
    all_work = Work.objects.all()
    print(all_work)
    return render(request, 'showcase/index.html', {'all_work': all_work})
    
    
# def index(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = WorkForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Work(docfile = request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect('http://127.0.0.1:8000/alzheimers/')

#     else:

#         form = WorkForm() # A empty, unbound form
#         # Load documents for the list page
#         all_work = Work.objects.all()
#         #documents=DocumentForm().
#         # Render list page with the documents and the form
#         return render( 'showcase/index.html', {'all_work': all_work, 'form': form,},
#             context_instance=RequestContext(request)
#         )
