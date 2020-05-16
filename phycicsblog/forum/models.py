from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Nie odpowiedziano"),
    (1,"Opublikowano")
)

class Comment(models.Model):
    temat = models.CharField(max_length=300, unique=True)
    tresc = models.TextField()
    odpowiedz = models.TextField()
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='forum_posts')
    zmodyfikowano = models.DateTimeField(auto_now= True)
    dodano = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-dodano']

    def __str__(self):
        return self.temat
