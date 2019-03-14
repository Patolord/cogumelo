from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from news.models import Post

def index(request):
    posts = Post.objects.order_by('-created_at').filter(is_published=True)

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts
    }

    return render(request, 'pages/news.html', context)

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'pages/post.html', {'post': post})