from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def about(request):
    return HttpResponse(f"About view {request.user}")