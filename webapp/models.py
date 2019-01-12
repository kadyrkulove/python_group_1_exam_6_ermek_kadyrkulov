from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='UserInfo', verbose_name='Пользователь')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    photo = models.ImageField(verbose_name='Фотография', null=True, blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name="friends", verbose_name="Друзья")

    def __str__(self):
        return self.phone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts_by_user', verbose_name='Автор поста')

    def __str__(self):
        return self.title