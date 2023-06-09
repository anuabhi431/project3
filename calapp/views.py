from django.shortcuts import render
from django.http import Http Response
# Create your views here.
def home(request):
    x=request.POST["G1"]
    y=request.POST["G2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=Http Response("THE SUM IS :"+str(z))
    return res
