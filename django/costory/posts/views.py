from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return redirect('post_list')


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)
    return render(request, 'posts/post_list.html', {'page': page})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('post_detail', post_id=new_post.id)
    else:
        post_form = PostForm()
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    else:
        return render(request, 'posts/post_confirm_delete.html', {'post': post})
