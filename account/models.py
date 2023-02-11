from django.conf import settings
from django.db import models


class Links(models.Model):
    full_link = models.URLField('Полная ссылка', max_length=500)
    short_link = models.CharField('Сокращенная ссылка', max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
