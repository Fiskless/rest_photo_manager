
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField("Фото", upload_to="photos/")
    geo_location = models.CharField("Геолокация", max_length=100, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    people_names = ArrayField(
        models.CharField(max_length=50, blank=True),
        default=[]
    )
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
