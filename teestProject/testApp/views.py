from django.shortcuts import render

# Create your views here.
def test3(request):
    return render(request, 'test3.html')

# Create your views here
def test2(request):
    return render(request, 'test2.html')
