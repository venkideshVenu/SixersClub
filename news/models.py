from django.db import models
from django.utils import timezone
from accounts.models import CustomUser  # Import the CustomUser model from the accounts app

class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser as the author
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='article_photos/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
