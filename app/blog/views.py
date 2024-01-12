from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.
class HomepageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"
