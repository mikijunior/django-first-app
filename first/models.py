from django.db import models


class Article(models.Model):
    title = models.CharField('article title', max_length=255)
    text = models.TextField('article text')
    pub_date = models.DateTimeField('publish date')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('comment author', max_length=50)
    comment = models.CharField('comment text', max_length=255)

    def __str__(self):
        return self.comment
