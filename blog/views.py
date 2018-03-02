from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import Category, Post, Tag
import markdown


def PostList(request):
    objects_list = Post.published.all()
    paginator = Paginator(objects_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'bootstrap/post/index.html', {'page': page, 'posts': posts})


def PostDetail(request, year, month, day, title):
    post = get_object_or_404(Post,
                             title=title,
                             status='p',
                             pub_time__year=year,
                             pub_time__month=month,
                             pub_time__day=day)
    post.increase_views()

    md = markdown.Markdown(extensions=[
                           'markdown.extensions.extra',
                           'markdown.extensions.codehilite',
                           'markdown.extensions.toc'])
    post.body = md.convert(post.body)

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id = post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-pub_time')[:5]

    return render(request, 'bootstrap/post/detail.html', {'post': post, 'toc': md.toc, 'similar_posts': similar_posts})


def CateList(request):
    categories = Category.objects.all()
    return render(request, 'bootstrap/post/categories.html', {'categories': categories})


def CateDetail(request, cate):
    cate_posts = Post.objects.filter(category__name=cate)
    return render(request, 'bootstrap/post/catedetail.html', {'cate_posts': cate_posts})


def Archives(request):
    archives = Post.objects.all().order_by('-pub_time')
    return render(request, 'bootstrap/post/archives.html', {'archives': archives})


def AboutMe(request):
    print('into about page')
    return render(request, 'bootstrap/post/about.html')


def TagList(request):
    tags = Tag.objects.all()
    return render(request, 'bootstrap/post/tags.html', {'tags': tags})


def TagDetail(request, tag):
    tag_posts = Post.published.filter(tags__name=tag)
    return render(request, 'bootstrap/post/tagdetail.html', {'tag_posts': tag_posts})