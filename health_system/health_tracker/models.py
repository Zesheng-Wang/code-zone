from django.db import models
from django.utils import timezone

class WeightRecord(models.Model):
    weight = models.DecimalField("体重(kg)", max_digits=5, decimal_places=2)
    height = models.DecimalField("身高(m)", max_digits=3, decimal_places=2, default=1.70)
    date = models.DateField("记录日期", default=timezone.now)
    note = models.TextField("备注", blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "体重记录"
        verbose_name_plural = "体重记录"

    def __str__(self):
        return f"{self.date} - {self.weight}kg"

    @property
    def bmi(self):
        return round(float(self.weight) / (float(self.height) ** 2), 1)