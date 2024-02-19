from django.db import models

class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    text = models.TextField('Содержимое')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        # verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
