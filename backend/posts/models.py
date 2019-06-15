from django.db import models


class Post(models.Model):
    # autofield is added by django for primary key
    # id = models.AutoField()
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        ordering = ('id',)
