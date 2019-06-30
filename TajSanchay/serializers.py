from rest_framework import serializers
from loan.models import Loan

class loanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'