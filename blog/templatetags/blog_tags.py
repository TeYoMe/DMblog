import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from ..models import Post, Category, Tag


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown.markdown(value,
                                       extensions=['markdown.extensions.fenced_code',
                                                   'markdown.extensions.codehilite',
                                                   'markdown.extensions.toc', ],
                                       safe_mode=True,
                                       enable_attributes=False))


@register.simple_tag
def catepost_count(cate):
    return Post.published.filter(category__name=cate).count()


@register.assignment_tag
def get_latest_posts():
    return Post.published.order_by('-pub_time')[:10]


@register.assignment_tag
def most_views_posts():
    return Post.published.order_by('-views')[:10]


@register.simple_tag
def allpost_count():
    return Post.published.all().count()


@register.simple_tag
def allcate_count():
    return Category.objects.all().count()


@register.simple_tag
def alltag_count():
    return Tag.objects.all().count()
