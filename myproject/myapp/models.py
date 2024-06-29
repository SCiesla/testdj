from django.db import models

class MyTableExcel(models.Model):
    data = models.CharField(max_length=255)
