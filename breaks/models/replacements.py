from django.db import models

import breaks.models.groups


class Replacement(models.Model):
    group = models.ForeignKey(
        'breaks.Group',
        models.CASCADE,
        related_name='replacements',
        verbose_name='Группа'
    )
    date = models.DateField('Дата смены')
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    break_max_duration = models.PositiveSmallIntegerField('Максимальная длительность обеда')

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-date',)

    def __str__(self):
        return f'Смена №{self.pk} для {self.group}'


class ReplacementStatus(models.Model):
    code = models.CharField('Код', max_length=16, primary_key=True)
    name = models.CharField('Название', max_length=32, )
    sort = models.PositiveSmallIntegerField('Сортировка', null=True, blank=True)
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        verbose_name = 'Статус_смены'
        verbose_name_plural = 'Статусы_смены'
        ordering = ('sort',)

    def __str__(self):
        return f'Смена №{self.code} для {self.name}'
