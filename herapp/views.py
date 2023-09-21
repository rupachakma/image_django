from django.shortcuts import render
from . models import People

# Create your views here.
def home(request):

    data={}
    if request.method == "POST":
        a=request.POST.get("n1")
        b=request.POST.get("a1")
        img=request.FILES["imagefile"]
        data={
            'x':a,
            'y':b,
        }

        info=People()
        info.name=a
        info.address=b
        info.profileImg=img
        info.save()


    return render(request,"index.html",data)

def view_data(request):
    people_data = People.objects.all()
    return render(request, "view_data.html", {'people_data':people_data})