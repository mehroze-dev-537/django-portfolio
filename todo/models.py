from django.db import models

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
