from django.shortcuts import render

# Create your views here.
def v_home_page(request):
    return render(request, 'index.html')
