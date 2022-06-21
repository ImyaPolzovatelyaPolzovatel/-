from django.db import models

# Create your models here.
class modelNews(models.Model):
    title = models.CharField('Название', max_length=30)
    descriptionShort  =  models.CharField('Краткое описание', max_length=20)
    image = models.ImageField(null=True, blank=True,upload_to="images/", verbose_name=u'Изображение',)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'