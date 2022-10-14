from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'baabtra/baabtrahome.html') 

def page1(request):
    return render(request,'baabtra/baabtrapage1.html')

def aboutus(request):
    return render(request,'baabtra/aboutuspage.html')   

def css(request):
    return render(request,'baabtra/css.html') 

def css2(request):
    return render(request,'baabtra/css2.html')   

def grid(request):
    return render(request,'baabtra/grid.html')    

def grid2(request):
    return render(request,'baabtra/grid2.html')

def bootstrap(request):
    return render(request,'baabtra/bootstrap.html')

def bootstrap2(request):
    return render(request,'baabtra/bootstrap2.html')

def bootstrap3(request):
    return render(request,'baabtra/bootstrap3.html')



