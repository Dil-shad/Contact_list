
from django.shortcuts import redirect, render
from .models import *
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):

    obj = PhoneBookModel.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'index.html', context)

@csrf_exempt
def create_contact(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        cmobile = request.POST['cmob']
        if request.FILES.get('file') is not None:
            image = request.FILES['file']
        else:
            image = "/static/image/default.png"

        cmdl = PhoneBookModel(
            name=cname,
            mobile=cmobile,
            image=image,
        )
        cmdl.save()
        return redirect('index')
    return render(request, 'create_contact.html')


def view_contact(request, pk):

    print(pk)
    cmdl = PhoneBookModel.objects.get(id=pk)
    return render(request, 'view_contact.html', {'obj': cmdl})


def edit_contact(request, pk):
    if request.method == 'POST':
        e = PhoneBookModel.objects.get(id=pk)
        e.name = request.POST.get('cname')
        e.mobile = request.POST.get('c_no')
        if request.FILES.get('file') is not None:
            e.image = request.FILES.get('file')
        else:
            pass
        e.save()
        return redirect('index')
    cmdl = PhoneBookModel.objects.get(id=pk)
    return render(request, 'edit_contact.html', {'obj': cmdl})


def contact_delete(request, pk):
    var = PhoneBookModel.objects.get(id=pk)
    print('pop')
    if var.image is not None:
        if not var.image == "/static/image/default.png":
            os.remove(var.image.path)
        else:
            pass
    var.delete()
    return redirect('index')