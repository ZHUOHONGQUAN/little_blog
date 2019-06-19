from django.db import models

# Create your models here.

class Article(models.Model):

    article_id = models.AutoField(primary_key=True)  #文章的唯一ID

    title = models.TextField() #文章的标题

    brief_content = models.TextField()  #文章的简要

    content = models.TextField()  #文章的主要内容

    publish_date =  models.DateTimeField(auto_now=True)  #文章的发布日期



    def __str__(self):
        return self.title