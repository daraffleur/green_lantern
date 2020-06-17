from django.db import models
from django.utils.translation import gettext_lazy as _



class NewsLetter(models.Model):
    email = models.EmailField(max_length=100)


    class Meta:
        ordering = ["email"]

        verbose_name = _("NewsLetter")
        verbose_name_plural = _("NewsLetters")

    def __str__(self):
        return self.email
