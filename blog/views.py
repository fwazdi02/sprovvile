from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Category, Comment
from .forms import CommentForm
from django.contrib import messages


class PostList(ListView):
    queryset = Post.objects.publish()
    context_data = {
        'category': Category.objects.filter(is_active=True),
    }
    extra_context = {
        'page_title':'Blog',
    }

class PostDetail(DetailView, FormMixin):
    model = Post
    form_class = CommentForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    extra_context = {
        'page_title':'Blog',
    }

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        comment = Comment.objects.select_related('post') \
            .filter(post__slug=self.kwargs.get('slug'), status='publish')
        context['comments'] = comment
        context['comment_form'] = CommentForm
        return context
    

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid:
            post = Post.objects.filter(pk=int(request.POST.get('post_id'))).first()
            form.instance.post = post
            form.save()
            messages.success(request, '*** Form submission successful ***')
    return HttpResponseRedirect("{}#comment".format(reverse('blog:single', kwargs={'slug':post.slug})))

