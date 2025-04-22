from django.db import models


# Create your models here.
class ProjectCategory(models.Model):
    """Modelo para categorias de projetos.

    Args:
        models (Model): Classe base de modelo do Django

    Returns:
        ProjectCategory: Uma instância de categoria de projeto
    """

    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Configurações de metadados para o modelo ProjectCategory"""

        verbose_name = 'Categoria de Projeto'
        verbose_name_plural = 'Categorias de Projetos'

    def __str__(self):
        """Retorna a representação em string do objeto

        Returns:
            str: Nome da categoria
        """
        return self.name


class Project(models.Model):
    """Modelo para projetos do portfólio.

    Args:
        models (Model): Classe base de modelo do Django

    Returns:
        Project: Uma instância de projeto
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)
    categories = models.ManyToManyField(ProjectCategory)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna a representação em string do objeto

        Returns:
            str: Título do projeto
        """
        return self.title
