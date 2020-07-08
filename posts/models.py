from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Your text')
    image = models.ImageField(verbose_name='Image', upload_to='post_images/', null=True, blank=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now, verbose_name='Published')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    draft = models.BooleanField(default=False, verbose_name='Draft')
    liked_by = models.ManyToManyField(User, through='Like', related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post',
        verbose_name_plural = 'Posts'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.user

