from pyexpat import model
from rest_framework import serializers
from uploadAPI.models import profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'