import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Post
from .form import CommentForm, NewPostForm, UploadImage
from authorization.models import AppUser


class IndexView(View):
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        tags = request.GET.get('tags')
        post_list = Post.objects.all().order_by('-date')

        if tags is not None:
            post_list = post_list.filter(tags__regex=tags)
        paginator = Paginator(post_list, 10)

        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request, 'blog/index.html', context={
            'posts': posts,
            'user': user
        })


class ShowPost(LoginRequiredMixin, View):
    login_url = reverse_lazy('authorization:login')
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        post = Post.objects.all().get(pk=kwargs['pk'])
        comment_form = CommentForm()

        return render(request, 'blog/show_post.html', context={
            'post': post,
            'comment_form': comment_form
        })

    def post(self, request, *args, **kwargs):
        user = request.user
        post_id = kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            print('***')
            print(user)
            print('***')
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = user
            comment.save()
            return HttpResponseRedirect(reverse('blog:certain_post', kwargs={'pk': kwargs['pk']}))


class PostView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authorization:login')
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        form = NewPostForm()

        return render(request, 'blog/new_post.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        user = request.user
        new_post_form = NewPostForm(request.POST)

        if new_post_form.is_valid():
            post = new_post_form.save(commit=False)
            post.author = user
            post.tags = json.dumps(request.POST.get('tags'))
            post.save()

            return HttpResponseRedirect(reverse('blog:index'))


class ShowUser(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        form = UploadImage()

        return render(request, 'blog/profile.html', context={
            'user': user,
            'form_img': form
        })

    def post(self, request, *args, **kwargs):
        user = AppUser.objects.get(pk=request.user.pk)
        form = UploadImage(files=request.FILES)
        if form.is_valid():
            user.avatar = request.FILES['file']
            user.save()

        return HttpResponseRedirect('/')