from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from posts.models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    succes_url = reverse_lazy('home')

class DashboardView(ListView):
    template_name = 'dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()