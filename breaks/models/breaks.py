from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Break(models.Model):
    replacement = models.ForeignKey(
        'breaks.Replacement',
        models.CASCADE,
        related_name='breaks',
        verbose_name='Смены'
    )
    employee = models.ForeignKey(
        User,
        models.CASCADE,
        related_name='breaks',
        verbose_name='Сотрудник'
    )
    break_start = models.TimeField('Начало обеда')
    break_end = models.TimeField('Конец обеда')
    #duration = models.PositiveSmallIntegerField('Продолжительность', null=True, blank=True)
    break_max_duration = models.PositiveSmallIntegerField('Максимальная длительность обеда')
    status = models.ForeignKey('breaks.BreakStatus', models.CASCADE, 'breaks', verbose_name='Статус', blank=True)

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденные перерывы'
        ordering = ('-replacement__date', 'break_start')

    def __str__(self):
        return f'Обед пользователя: {self.employee} ({self.pk})'
