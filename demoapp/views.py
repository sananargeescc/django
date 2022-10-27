from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'index2.html')
def second(request):
    return render(request,'2nd.html')
