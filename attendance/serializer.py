from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Passcode
class PasscodeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passcode
        # json で出力するフィールド
        fields = ('passcode','created_at')