from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='article_photos/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
