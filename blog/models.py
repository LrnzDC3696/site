from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=69)
    date_posted = models.DateTimeField(default=timezone.now)
    context = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Post({self.title=}, {self.date_posted=})"


class Tag(models.Model):
    name = models.CharField(max_length=69)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Tag({self.name=})"
