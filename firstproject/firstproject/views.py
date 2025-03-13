from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data={
        'title':'Home-Page',
        'bdata':'Welcome to Home Page',
        'c_list': ['PHP','Python','Java','C++'],
        'student_details':[
            {'name':'Rahul','age':20},
            {'name':'Rohit','age':21},
            {'name':'Raj','age':22}
            ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("about page")
def contact(request):
    return HttpResponse("<h1>contact page</h1>")