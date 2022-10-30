from django.db import models
from datetime import datetime
# Create your models here.
class RewardPoints(models.Model):
    name = models.CharField(max_length=1000, default='')
    value = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'state'
        # Add verbose name
        verbose_name = 'Reward Point'
    def __str__(self):
        return self.name

class Log(models.Model):
    source = models.CharField(max_length=1000, default='')
    date = models.DateTimeField(default=datetime.now, blank = True)
