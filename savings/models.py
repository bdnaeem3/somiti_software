from django.db import models


class Savings(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11)
    nid = models.CharField(max_length=17)
    amount = models.CharField(max_length=4)
    join_date = models.DateField()

    def __str__(self):
        return self.name
