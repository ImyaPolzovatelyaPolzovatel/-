from django.db import models


# Create your models here.
class review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    message = models.TextField('Описание', blank=False)
    time_create = models.DateTimeField('Дата создания', auto_now_add=True)
    published = models.BooleanField('Опубликован', default=True)
    moderation = models.BooleanField('На модерации', default=False)
    deleted = models.BooleanField('Удален', default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'