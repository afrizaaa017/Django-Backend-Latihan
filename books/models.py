from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
    published_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)  # opsional
    updated_at = models.DateTimeField(auto_now=True)      # opsional

    def __str__(self):
        return f"{self.title} - {self.author}"
