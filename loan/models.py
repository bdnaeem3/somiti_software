from django.db import models
from reference.models import Reference


class Loan(models.Model):

    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=11, null=True)
    nid = models.CharField(max_length=17, null=True)
    amount = models.CharField(max_length=5, null=True)
    join_date = models.DateField(null=True)
    reference = models.ForeignKey(Reference, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, null=True, default=1)

    def __str__(self):
        return self.name
