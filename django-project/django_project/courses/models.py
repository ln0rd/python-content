from django.db import models
from django.urls import reverse
from django.conf import settings

class CourseManager(models.Manager):

    def search(self, query):
        ## return a list of
        return self.get_queryset().filter(name__icontains=query, description__icontains=query)

    def searchOr(self, query):
        return self.get_queryset().filter( 
            # or
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query) 
            )

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.CharField('Atalho', max_length=200)
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o Curso', null=True, blank=True)
    start_date = models.DateField('Data de inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    ## insert search and searchOr in Course.objects
    objects = CourseManager()

    def __str__(self):
        return self.name

    # create absolute URL per model
    def get_absolute_url(self):
        return reverse('details', args=(self.slug,))

    # effect in admin
    def Meta(parameter_list):
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["name"]

class Enrollment(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário',
        related_name='enrollments',
        on_delete = models.DO_NOTHING,
    )

    course = models.ForeignKey(
        Course, verbose_name='Curso', 
        related_name='enrollments',
        on_delete = models.DO_NOTHING,
    )

    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, 
        default=1, 
        blank=True,
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'course'),)