from django.db import models
from django.core.urlresolvers import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='p')


class Category(models.Model):
    name = models.CharField('分类名', max_length=30, unique=True)
    imgurl = models.CharField('分类图片', max_length=200, blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['name']
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('blog:CateDetail', args=[self.name])

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    COMMENT_STATUS = (
        ('O', '打开'),
        ('c', '关闭'),
    )

    title = models.CharField('标题', max_length=200, unique=True)
    category = models.ForeignKey('Category', verbose_name='分类', blank=False, null=False)
    tags = models.ManyToManyField('Tag', verbose_name='标签云', blank=True)
    views= models.PositiveIntegerField(default=0)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_mod_time = models.DateTimeField('修改时间', auto_now=True)
    pub_time = models.DateTimeField('发布时间', blank=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-pub_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        get_latest_by = 'created_time'

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:PostDetail',
                       args=[self.pub_time.year,
                             self.pub_time.strftime('%m'),
                             self.pub_time.strftime('%d'),
                             self.title])

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('标签', max_length=30, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:TagDetail', args=[self.name])

    class Meta:
        ordering = ['id']
        verbose_name = '标签'
        verbose_name_plural = verbose_name



