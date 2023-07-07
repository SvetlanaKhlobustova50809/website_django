from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, null=True)
    anons = models.CharField('Anons', max_length=250, null=True)
    full_text = models.TextField('List', null=True)
    date = models.DateTimeField('Date publications', null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'