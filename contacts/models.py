from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.EmailField('Email', max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
