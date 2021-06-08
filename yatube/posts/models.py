from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200, unique=True,
        help_text=('Группа, сообщество, подборка записей, суть одна, в этом '
                   'месте собраны сообщения, имеющие некую общность. '
                   'Название подборки призвано её отражать'),
        verbose_name='Название подборки'
    )
    slug = models.SlugField(
        unique=True,
        help_text=('Укажите адрес для страницы подборки. Используйте только '
                   'латиницу, цифры, дефисы и знаки подчёркивания'),
        verbose_name='Часть адресной строки для подборки'
    )
    description = models.TextField(
        help_text=('Краткое описание принципов объединения записей в '
                   'подборку, тематика и основные правила поведения'),
        verbose_name='Описание подборки'
    )

    class Meta:
        verbose_name = 'Подборка записей'
        verbose_name_plural = 'Подборки записей'
        ordering = ('pk',)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст записи'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts', verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='posts', verbose_name='Подборка записей'
    )
    image = models.ImageField(
        upload_to='posts/', blank=True, null=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Комментируемая запись'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Автор комментария'
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    created = models.DateTimeField(
        verbose_name='Датаи и время комметария',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author.username[:15]} {self.text[:20]}'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="follower", verbose_name='Подписчик'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="following", verbose_name='Автор записей'
    )

    class Meta:
        ordering = ('author',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    """def __str__(self):
        return (f'Подписчик {self.follower.username[:15]}'
                f' на автора {self.author.username[:15]}')"""
