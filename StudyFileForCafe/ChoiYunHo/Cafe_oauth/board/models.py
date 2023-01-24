from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    board = models.ForeignKey('Board', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    content = models.TextField()


    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=10, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user_name