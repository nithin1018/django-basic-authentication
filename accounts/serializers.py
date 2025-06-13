from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self,validate_data):
        user = User.objects.create_user(
            username=validate_data['username'],
            email=validate_data['email'],
            password=validate_data['password'],
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
        read_only_fields = ['username']
    def validate_username(self, value):
        user=self.context['request'].user
        if user.username == value:
            raise serializers.ValidationError("This is your current username")
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError("This Username is already taken")
        
    def update(self, instance, validated_data):
        # Safely update fields only if they're passed
        username = validated_data.get('username', instance.username)
        email = validated_data.get('email', instance.email)

        instance.username = username
        instance.email = email
        instance.save()
        return instance