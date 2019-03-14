from django.shortcuts import render
from news.models import Post

def index(request):
    lpost1 = Post.objects.order_by('-pk').filter(is_published=True)[0]
    lpost2 = Post.objects.order_by('-pk').filter(is_published=True)[1]
    lpost3 = Post.objects.order_by('-pk').filter(is_published=True)[2]
    return render(request, 'pages/index.html', {'lpost1' : lpost1,'lpost2' : lpost2,'lpost3' : lpost3, })

def about(request):
	return render(request, 'pages/about.html')