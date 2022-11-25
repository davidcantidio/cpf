from django.db import models

# Create your models here.


class Cpf(models.Model):
    nine_digit_cpf = models.IntegerField(max_length=9)
    def __str__(self):
        return f"{self.nine_digit_cpf}"
    