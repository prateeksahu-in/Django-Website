from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"this is sent",
        "var2":"this is 2nd var"
        }
    return render(request,'index.html',context)
    # return HttpResponse("This is home pager")


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
