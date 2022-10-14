from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'teacher/teacherhome.html')

def profile(request):
    return render(request,'teacher/teacherprofile.html')    
