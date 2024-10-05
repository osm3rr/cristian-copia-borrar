from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.TextField()
    author = models.ForeignKey("auth.User", 
        on_delete = models.CASCADE),

    class Meta:
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo