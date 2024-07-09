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
    return render(request,'index.html')
