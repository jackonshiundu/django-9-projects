from rest_framework import serializers
from .models import Moviedata


class Movieserializer(serializers.ModelSerializer):
    poster=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Moviedata
        fields=['id','name','duration','gener','rating','poster']