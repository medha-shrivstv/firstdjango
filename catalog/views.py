from django.shortcuts import render
from .forms import BookForms
from catalog.models import Book


# Create your views here.
'''def form_view(request):
    form=BookForms()
    context={
        "head":"Custom Form created here using python",
        "forms":form,
        

    }
    return render(request, 'forms.html',context)'''


def form_view(request):
    msg=''
    if request.method=='POST':
        form=BookForms(request.POST)
        if form.is_valid():

            book=Book(

                 name=form.cleaned_date.get('name'),
                 purchase_date=form.cleaned_data.get('purchase_get'),
                 genre=form.cleaned_data.get('genre'),
                 author=form.cleaned_data.get('author')
            )
            book.save()
            msg='Book added successfully'
        else:

             msg=form.errors()
    else:
        form=BookForms()
    return render(request, 'forms.html',{"msg":msg, "forms":form})
    
def html_form(request):
    if request.method=='POST':
        value=request.POST.get('uname')
        return render(request,'values.html',{'value':value})
    else:
        return render(request, 'login.html')