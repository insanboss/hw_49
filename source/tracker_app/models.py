from django.db import models


# Create your models here.

# status_choices = [('New', 'новый'), ('In Progress', 'в процессе'), ('Done', 'выполнено')]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Issue(BaseModel):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('tracker_app.Status', on_delete=models.PROTECT, max_length=50, verbose_name='Статус')
    type = models.ForeignKey('tracker_app.Type', on_delete=models.PROTECT, max_length=50, verbose_name='Тип')

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
