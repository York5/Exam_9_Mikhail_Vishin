from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='product_images', null=False, blank=False, verbose_name='Photo')
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date Added')
    likes = models.IntegerField(default=0, verbose_name='Likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Author',
                               related_name='photos')
    like_users = models.ManyToManyField(User, related_name='photos', through='webapp.Like',
                                        blank=True, verbose_name='User_Likes')

    def __str__(self):
        return self.description


class Comment(models.Model):
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    photo = models.ForeignKey('webapp.Photo', related_name='comments',
                              on_delete=models.CASCADE, verbose_name='photo')
    author = models.ForeignKey(User, null=False, blank=False, default=None, verbose_name='Автор',
                               on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text[:20]


class Like(models.Model):
    photo = models.ForeignKey('Photo', on_delete=models.PROTECT, null=True, blank=False, verbose_name='Photo',
                              related_name='photo_likes')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False, verbose_name='User',
                             related_name='user_likes')

