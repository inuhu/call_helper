from django.db import models

from common.models.mixins import BaseDictModelMixin


class ReplacementStatus(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Статус_смены'
        verbose_name_plural = 'Статусы_смены'



class BreakStatus(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Статус_обеда'
        verbose_name_plural = 'Статусы_обедов'


