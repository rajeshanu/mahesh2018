from django.shortcuts import render
from .models import product
# Create your views here.
def showindex(request):
    p1=product.objects.all()
    p3 = product.objects.last()
    id = 0
    if p3 == None:
        id = 100
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request,"index.html",{"emp":p1,"nam":id})


def getdetails(request):
    idno=request.POST.get("t1")
    nam=request.POST.get("t2")
    salary=request.POST.get("t3")
    #from .models import product
    p1=product(idno=idno,name=nam,salary=salary)
    p1.save()
    p1=product.objects.all()
    p3 = product.objects.last()
    id = 0
    if p3 == None:
        id = 100
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request,"index.html",{"emp":p1,"message":"i am saved","nam":id})


def delete(request):
    idno=request.POST.get("delete")
    product.objects.filter(idno=idno).delete()
    p1=product.objects.all()
    p3 = product.objects.last()
    id = 0
    if p3 == None:
        id = 100
    else:
        id = p3.idno
        id = (int(id) + 1)
    return render(request,"index.html",{"emp":p1,"nam":id})


def update(request):
    idno=request.GET.get("update")
    p2=product.objects.get(idno=idno)
    p1=product.objects.all()
    return render(request,"update.html",{"emp":p1,"p2":p2,"id":idno})


def updatenext(request):
    idno = request.GET.get("update")
    idno1 = request.POST.get("t1")
    nam = request.POST.get("t2")
    salary = request.POST.get("t3")
    product.objects.filter(idno=idno).update(idno=idno1,name=nam,salary=salary)
    p1 = product.objects.all()
    p3=product.objects.last()
    id=0
    if p3==None:
         id=100
    else:
         id=p3.idno
         id=(int(id)+1)
    return render(request,"index.html",{"msg":"updated Successfully","emp":p1,"nam":id})