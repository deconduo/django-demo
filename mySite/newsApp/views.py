from django.views.generic import ListView, CreateView
from .models import Article

class ArticleList(ListView):
    model = Article

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'content']
    success_url = '/'
