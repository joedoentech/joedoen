from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'jdcompany/index.html')

def test(request):
    return render(request,'jdcompany/test.html')