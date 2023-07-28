from django.db import models

class Post(models.Model):
    picture = models.ImageField(upload_to="post/")
    caption = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return str(self.id)
    

class Like(models.Model):
    is_Liked = models.BooleanField(default=False)
    posts = models.ForeignKey(post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    

class Comment(models.Model):
    text = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
