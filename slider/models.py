from django.db import models

# Create your models here.


class Slides(models.Model):
    """docstring for Slides"""
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
    slides = models.ImageField(upload_to='slider/images')
    title = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
