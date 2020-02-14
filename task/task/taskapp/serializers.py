from rest_framework import serializers
from . import models
class taskserializers(serializers.ModelSerializer):
    class Meta:
        fields=('title','description','end_date','status','comments')
        model=models.newtask