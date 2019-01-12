from webapp.models import Post, UserInfo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import PostForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class MainView(ListView):
    model = Post
    template_name = 'main_list.html'


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'main_list.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostForm

    def dispatch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_detail', kwargs={'pk': pk}))
        return super().dispatch(request, pk=pk)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def dispatch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if post.author != self.request.user:
            return HttpResponseRedirect(reverse('webapp:post_detail', kwargs={'pk': pk}))
        return super().dispatch(request, pk=pk)

    def get_success_url(self):
        return reverse('webapp:main_list')

class UserListView(ListView):
    model = UserInfo
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = UserInfo
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.user.posts_by_user.all().order_by('-date')
        return context