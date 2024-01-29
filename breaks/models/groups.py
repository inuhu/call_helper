from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    name = models.CharField('Название', max_length=255)
    organization = models.ForeignKey(
        'breaks.Organization',
        models.RESTRICT,
        'Groups',
        verbose_name='Организация'
    )
    manager = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='group_managers',
        verbose_name='Менеджер',
    )
    employees = models.ManyToManyField(
        User,
        'group_amployees',
        verbose_name='Сотрудники',
        blank=True
    )
    min_active = models.PositiveSmallIntegerField(
        'Минимальное количество активных сотрудников',
        null=True,
        blank=True,
    )
    break_start = models.TimeField(
        'Начало обеда',
        null=True,
        blank=True,
    )
    break_end = models.TimeField(
        'Конец обеда',
        null=True,
        blank=True,
    )
    break_max_duration = models.PositiveSmallIntegerField(
        'Максимальная длительность обеда',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)


    def __str__(self):
        return f'id:{self.pk} {self.name}'
