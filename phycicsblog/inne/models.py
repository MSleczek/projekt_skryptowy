from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Wstrzymane"),
    (1,"Opublikowano")
)

class Post(models.Model):
    tytul = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='inne_posts')
    zmodyfikowano = models.DateTimeField(auto_now= True)
    tresc = models.TextField()
    dodano = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-dodano']

    def __str__(self):
        return self.tytul
