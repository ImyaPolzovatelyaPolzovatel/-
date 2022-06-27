from django.db import models
from django.shortcuts import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class modelNews(models.Model):
    title = models.CharField('Название', max_length=20)
    description  =  models.CharField('Краткое описание', max_length=20)
    content = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', null=True, blank=True,upload_to='imagesNews')
    time_create = models.DateTimeField('Дата новости', auto_now_add=True)
    slug = models.SlugField('URL', unique=True, db_index=True, max_length=255)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('newsInfo', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
        
class modelСategory(MPTTModel):
    name = models.CharField('Название', unique=True, max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='Потомок')
    image = models.ImageField('Изображение', null=True, blank=True,upload_to='imagesСategory')
    slug = models.SlugField('URL', unique=True, db_index=True, max_length=255)
    deleted = models.BooleanField('Удалено',default=False)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('categoryInfo', kwargs={'сategory_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    class MPTTMeta:
        order_insertion_by = ['name']
        

        
class modelProduct(models.Model):
    title = models.CharField('Название', max_length=20)
    cat= models.ForeignKey('modelСategory', on_delete=models.PROTECT, verbose_name='Категория')
    image = models.ImageField('Изображение', null=True, blank=True,upload_to='imagesProduct')
    slug = models.SlugField('URL', unique=True, db_index=True, max_length=255)
    content = models.TextField('Описание', blank=True)
    сharacteristics = models.TextField('Характеристики', blank=True)
    price = models.DecimalField('Цена', max_digits=16, decimal_places=10)
    act= models.ForeignKey('modelAction', on_delete=models.PROTECT, verbose_name='Акция')
    deleted = models.BooleanField('Удалено', default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('productInfo', kwargs={'product_slug': self.slug})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
        
class modelAction(models.Model):
    title = models.CharField('Название', max_length=20) 
    slug = models.SlugField('URL', unique=True, db_index=True, max_length=255)
    content = models.TextField('Описание', blank=True)
    deleted = models.BooleanField('Удалено', default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('actionInfo', kwargs={'action_slug': self.slug})
    
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'