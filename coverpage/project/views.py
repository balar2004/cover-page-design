from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

def coverpage(request):
    return render(request,"html/coverpage.html")