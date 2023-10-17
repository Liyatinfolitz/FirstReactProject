from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    # def validate_employeeID(self, value):
    #     """
    #     Check if the employeeID is unique.
    #
    #     This method is called when validating the 'employeeID' field.
    #     """
    #     if User.objects.filter(employeeID=value).exists():
    #         raise serializers.ValidationError("Employee ID must be unique.")
    #     return value


class PojectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    userID = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)  # Accept an array of user IDs

    class Meta:
        model = Members
        fields = '__all__'
