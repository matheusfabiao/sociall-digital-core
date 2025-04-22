from django.db import models


# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria de Projeto'
        verbose_name_plural = 'Categorias de Projetos'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(ProjectCategory)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
