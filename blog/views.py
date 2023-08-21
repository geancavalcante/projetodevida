from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def pagina(request):
    return render(request, 'pagina.html')