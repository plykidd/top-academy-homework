from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    completed = models.BooleanField()
    test = models.BooleanField()
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=100)