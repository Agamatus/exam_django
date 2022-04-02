from django.db import models


# Create your models here.

class ContactUsForm(models.Model):
    name = models.CharField(max_length=32, verbose_name="User's Name", null=False)
    email = models.EmailField(verbose_name="User's Email", null=False, unique=True)
    message = models.TextField(verbose_name="User's Message", max_length=300)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Call back contact'
        verbose_name_plural = 'Call back'

    def is_valid(self):
        pass


class Portfolio(models.Model):
    image = models.ImageField(
        verbose_name="Image",
        upload_to="media/portfolio"
    )

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
