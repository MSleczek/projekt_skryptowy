from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Wstrzymane"),
    (1,"Opublikowano")
)

class Post(models.Model):
    tytul = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE)
    zmodyfikowano = models.DateTimeField(auto_now= True)
    tresc = models.TextField()
    plik_1 = models.FileField(upload_to='upload_file/', default='default.pdf')
    plik_2 = models.FileField(upload_to='upload_file/', default='default.pdf')
    plik_3 = models.FileField(upload_to='upload_file/', default='default.pdf')
    plik_4 = models.FileField(upload_to='upload_file/', default='default.pdf')
    zdjecie_1 = models.ImageField(upload_to='upload_img/', default='default.jpg')
    zdjecie_2 = models.ImageField(upload_to='upload_img/', default='default.jpg')
    zdjecie_3 = models.ImageField(upload_to='upload_img/', default='default.jpg')
    dodano = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-dodano']

    def __str__(self):
        return self.tytul


