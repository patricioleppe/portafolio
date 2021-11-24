from django.db import models

#crear una clases y que herede 
# la Super Clase models.Model
class Project (models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="project")
    link = models.URLField(verbose_name="Direccion web",null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    # Esta clase es para darle los nombres al proyecto
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        # el - antes de created_at  es para darle orden descedente
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title