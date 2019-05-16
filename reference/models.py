from django.db import models
# from savings.models import Savings


class Reference(models.Model):
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=11, null=True)
    nid = models.CharField(max_length=17, null=True)
    # savings = models.OneToOneField(Savings, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(self.name)
