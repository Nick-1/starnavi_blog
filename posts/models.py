from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Your text')
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
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
    created = models.DateField(auto_now_add=True, verbose_name='Created')

    class Meta:
        unique_together = [['user', 'post']]

    def __str__(self):
        return f'user_id: {self.user.id} | post_id: {self.post_id}'
