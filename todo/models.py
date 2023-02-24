from django.db import models

# Create your models here.

Choice = (("danger", "high"), ("warning", "normal"), ("info", "low"))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=Choice
    )
    due_date = models.DateField()

    def __str__(self):
        return self.title
