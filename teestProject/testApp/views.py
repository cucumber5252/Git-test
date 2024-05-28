from django.shortcuts import render

# Create your views here.
def test3(request):
    return render(request, 'test3.html')