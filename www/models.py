from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    createt_at = models.DateTimeField(auto_now_add=True)

    @property
    def category(self):
        return "Love"
