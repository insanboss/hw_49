from django.conf import settings
from django.db import models

from tracker_app.validator import BadWordsValidation, capital_letter, MinLengthValidator

bad_words = ('fuck', 'bullshit', 'asshole')

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Issue(BaseModel):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок',
                               validators=[BadWordsValidation(bad_words), capital_letter, MinLengthValidator(10)])
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Описание',
                                   validators=[BadWordsValidation(bad_words)])
    status = models.ForeignKey('tracker_app.Status', on_delete=models.PROTECT, max_length=50, verbose_name='Статус')
    type = models.ManyToManyField('tracker_app.Type', related_name='issues', blank=True, verbose_name='Тип')
    project = models.ForeignKey('tracker_app.Project', related_name='project_issues', on_delete=models.CASCADE,
                                verbose_name='Проект')

    class Meta:
        db_table = 'issues'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)


class Status(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Project(models.Model):
    start_time = models.DateField(null=False, blank=False)
    end_time = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name='projects',
        verbose_name='Пользователь',
    )

    class Meta:
        permissions = [
            ('add_user_to_project', 'Добавить пользователя к проекту')
        ]

    def __str__(self):
        return "{}".format(self.title)
