from django.db import models




class todo(models.Model):
    text =models.CharField(max_length=50)
    finish = models.BooleanField(default=False)

    def __str__(self):
        return self.text