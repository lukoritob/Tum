from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from bmcs.forms import UserRegisterForm, DocumentForm
from django.contrib import messages
from django.forms import ModelForm
from .models import UpcomingTenders,VendorsTable,Document,Bids
from django.utils.encoding import smart_str
from django.views.generic import CreateView
from .models import Document
import datetime

@login_required
def download(request,doc):
    documents = UpcomingTenders.objects.all()
    response = ''
    for i in documents:
        if int(i.id) == int(doc):
            path = str(i.document)
            response = HttpResponse(content_type='application/force-download')  
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(path)
            response['X-Sendfile'] = smart_str(path)
    return response

@login_required
def delete(request,doc):
    UpcomingTenders.objects.get(id= doc).delete()
    return redirect('dashboard')

@login_required
def details(request,doc):
    document = UpcomingTenders.objects.get(id= doc)
    return render(request, 'bmcs/more.html',{'document':document }) #, 'bids' : bids

@login_required
def addTender(request):
    if request.method == 'POST':
        document=UpcomingTenders()
        print(document)
        document.Vendors_Name =     request.POST.get('owner')
        document.Project_Name =     request.POST.get('name')
        document.Basic_Amount_Ksh = request.POST.get('amount')
        document.Project_Type =     request.POST.get('project_type')
        document.Bid_Close_Date =   request.POST.get('deadline')
        document.Tender_Type =      request.POST.get('type')
        document.document  =        request.POST.get('document') #request.POST.get('document')
        document.save()
        return redirect('dashboard')  
    else:
        return render(request, 'bmcs/addTender.html')

    return render(request, 'bmcs/addTender.html')



@login_required
def dashboard(request):
    tenders = UpcomingTenders.objects.all()
    return render(request, 'bmcs/dashboard.html',{'tenders': tenders})


def register(request):
    if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login_url')
    else:
        form = UserRegisterForm()
    return render(request, 'bmcs/register.html',{'form':form})


@login_required
def bid(request, doc):
    tender = UpcomingTenders.objects.get(id= doc)
    if request.method == 'POST':
        bid = Bids()
        bid.tender = tender
        bid.text = request.POST.get('text')
        bid.author = request.user
        bid.save()
        return redirect('more', doc)  
    else:
        return render(request, 'bmcs/bid.html' ,{ 'tender' : doc})  

