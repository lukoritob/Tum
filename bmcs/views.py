from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from bmcs.forms import UserRegisterForm, DocumentForm
from django.contrib import messages
from django.forms import ModelForm
from .models import UpcomingTenders,VendorsTable,Document
from django.utils.encoding import smart_str


# Create your views here.
def aboard(request):
    documents = Document.objects.all()
    #print(paths)
    return render(request, 'bmcs/aboard.html', {'documents':documents})

def board(request,doc):
    documents = Document.objects.all()
    response = ''
    for i in documents:
        print(i.id)
        if int(i.id) == int(doc):
            path = str(i.document)
            print(path)
            response = HttpResponse(content_type='application/force-download')  
            response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(path)
            response['X-Sendfile'] = smart_str(path)
    return response


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doc')
    else:
        form = DocumentForm() #if the request is a get request we instantiate an empty form
    return render(request, 'bmcs/model_form_upload.html', {'form':form})


def indexView(request):
    return render(request, 'bmcs/home.html')


@login_required
def dashboardView(request):
    trial1 = UpcomingTenders.objects.all()
    context={
        'trial1':trial1
    }
    return render(request, 'bmcs/display1.html',context)


def registerView(request):
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

def bid(request):
    context = {
    }
    return render(request,'bmcs/bid.html',context)
class UpcomingTendersForm(ModelForm):
    class Meta:
        model = UpcomingTenders
        fields = '__all__'
def query1(request):
        trial1 = UpcomingTenders.objects.all()
        form = UpcomingTendersForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'trial1':trial1,
            'form':form
        }
        return render(request, 'bmcs/input1.html' ,context)
# def query1(request):
#     if request.method == "GET":
#         if id==0:
#             form = UpcomingTendersForm()
#         else:
#             retrieve = UpcomingTenders.objects.get(pk=id)
#             form = UpcomingTendersForm(instance=retrieve)
#         return render(request, "angel/input1.html",{'form':form})
#     else:
#         form = UpcomingTendersForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/input1/input1')
class VendorsTableForm(ModelForm):
    class Meta:
        model = VendorsTable
        fields = '__all__'
def query2(request):
        trial2 = VendorsTable.objects.all()
        form = VendorsTableForm(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'trial2':trial2,
            'form':form
        }
        return render(request,'bmcs/input2.html',context)

def query3(request):
        context = {
        }
        return render(request,'bmcs/input3.html',context)

def query4(request):
    context = {
    }
    return render(request,'bmcs/input4.html',context)

def query5(request):
    context = {
    }
    return render(request,'bmcs/input5.html',context)

def deleteme1(request, Tender_Id):
    employee=UpcomingTenders.objects.get(pk=Tender_Id)
    employee.delete()
    return redirect('/bmcs/display1')
    
def edit(request):
    context = {
    }
    return render(request,'bmcs/edit.html',context)

def deleteme3(request):
    context = {
    }
    return render(request,'bmcs/delete3.html',context)

def deleteme4(request):
    context = {
    }
    return render(request,'bmcs/delete4.html',context)

def deleteme5(request):
    context = {
    }
    return render(request,'bmcs/delete5.html',context)

def display1(request):
    trial1 = UpcomingTenders.objects.all()
    context={
        'trial1':trial1
    }
    return render(request, 'bmcs/display1.html',context)
def display2(request):
    trial2 = VendorsTable.objects.all()
    context = {
        'trial2':trial2
    }
    return render(request, 'bmcs/display2.html',context)
def display3(request):
    context ={
    }
    return render(request, 'bmcs/display3.html',context)
def display4(request):
    context={
        
    }
    return render(request,'bmcs/display4.html',context)
def display5(request):
    context = {
        
    }
    return render(request, 'bmcs/display5.html',context)