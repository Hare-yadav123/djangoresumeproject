from django.shortcuts import render

# Create your views here.
def service(request):
    serve={'service':'active'}
    return render(request,'serve/service.html',serve)
