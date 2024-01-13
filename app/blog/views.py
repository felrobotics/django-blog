from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
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


def post_single(request, post):
    post = get_object_or_404(Post, slug=post)
    related = Post.objects.filter(author=post.author)[:5]  # limit to only 5
    return render(request, "blog/single.html", {"post": post, "related": related})


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        # return Post.objects.all()  # return all, for debugging

        # not working because slug (python) does not match name (Python) which is capitalized
        # return Post.objects.filter(tags__name=self.kwargs["tag"])
        return Post.objects.filter(tags__slug__in=[self.kwargs["tag"]])

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements-tags.html"
        return "blog/tags.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(TagListView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag"]
        return context
