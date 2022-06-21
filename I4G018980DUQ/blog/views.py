from django.views.generic.edit import CreateView
from .models import blog

# Create your views here.
class PostListView(generic.ListView):
    model = blog
    

class PostCreateView(CreateView):
    model = blog
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDetailView(DetailView):
    model = blog
    

class PostUpdateView(UpdateView):
    model = blog
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')


class PostDeleteView(UpdateView):
    model = blog
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')