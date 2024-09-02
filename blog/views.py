from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Post
from django.views.generic import DetailView

def post_list(request):
    posts = Post.objects.all().order_by('-publication_date')
    return render(request, 'post_list.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


def home(request):
    return render(request, 'blog/post_page.html')



class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10  

    def get_queryset(self):
        queryset = super().get_queryset()
        fecha = self.request.GET.get('fecha_publicacion')
        categoria = self.request.GET.get('categoria')
        if fecha:
            queryset = queryset.filter(fecha_publicacion=fecha)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        # Búsqueda por título o contenido
        busqueda = self.request.GET.get('q')
        if busqueda:
            queryset = queryset.filter(
                Q(titulo__icontains=busqueda) | Q(contenido__icontains=busqueda)
            )
        return queryset