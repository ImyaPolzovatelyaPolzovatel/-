from django.db import models
from django.shortcuts import reverse

# Create your models here.
class modelNews(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Краткое описание', max_length=20)
    content = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', null=True, blank=True, upload_to='imagesNews')
    time_create = models.DateTimeField('Дата новости', auto_now_add=True)
    slug = models.SlugField('URL', unique=True, db_index=True, max_length=255)
    deleted = models.BooleanField('Удалено', default=False)
    show_on_manepage = models.BooleanField('Показывать на главной странице', default=False)
    show_on_footer = models.BooleanField('Показывать на футере', default=False)

    # по галк фильтровать
    # jquery, сделать вьюху, которая будет
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsInfo', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'