from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class IronConcentrate(models.Model):
    name = models.CharField(max_length=60)
    iron = models.DecimalField(max_digits=10, decimal_places=5)
    silicon = models.DecimalField(max_digits=10, decimal_places=5)
    aluminium = models.DecimalField(max_digits=10, decimal_places=5)
    calcium = models.DecimalField(max_digits=10, decimal_places=5)
    sulfur = models.DecimalField(max_digits=10, decimal_places=5)
    months = [
        (1, 'Январь'), (2, 'Февраль'),
        (3, 'Март'), (4, 'Апрель'),
        (5, 'Май'), (6, 'Июнь'),
        (7, 'Июль'), (8, 'Август'),
        (9, 'Сенябрь'), (10, 'Октябрь'),
        (11, 'Ноябрь'), (12, 'Декабрь'),
    ]
    month = models.IntegerField(choices=months)

    class Meta:
        verbose_name = "IronConcentrate"
        verbose_name_plural = "IronConcentrates"

    def __str__(self):
        return f'{self.id} {self.name} {self.iron}'
