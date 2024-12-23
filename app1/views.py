from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,'demo.html')
def code(request):
    return render(request,'code.html')
def home(request):
    return render(request,'home.html')
def course(request):
    return render(request,'course.html')
def boot(request):
    return render(request,'boot.html')
def call(request):
    return render(request,'call.html')
def sign(request):
    return render(request,'sign.html')
def impact(request):
    return render(request,'impact.html')
def email(request):
    return render(request,'email.html')