from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=160)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('authorization.AppUser', related_name='post_author')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comment')
    author = models.ForeignKey('authorization.AppUser', related_name='comment_author')
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text