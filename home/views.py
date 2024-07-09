from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("""
#                         <h1>Hey I am a Django Server</h1>
#                         <p>This is for multiple html</p>
#                         <hr>
#                         """)

# def sucess_page(request):
#     print("*****")
#     return HttpResponse("<h1> THIS IS SUCCESS PAGE <h1>")

def home(request):

    peoples=[
        {'name':'rohit sharma','age':24},
        {'name':'dev patel','age':15},
        {'name':'jay doshi','age':30}
    ]
    
    return render(request,'index.html',context={'peoples':peoples})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

