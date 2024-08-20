from django.utils.translation import gettext_lazy as _
from django.db import models

from django_resized import ResizedImageField


class Gallery(models.Model):
    name = models.CharField("name", max_length=256)
    description = models.CharField("description", max_length=256)
    image = ResizedImageField(
        size=[466, 360], crop=["middle", "center"], upload_to="gallery/%Y/%m"
    )

    class Meta:
        db_table = "gallery"
        verbose_name = _("gallery")
        verbose_name_plural = _("galleries")

    def __str__(self):
        return f"{self.name}"
