from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    admin_code = serializers.CharField(write_only=True,required=False)
    class Meta:
        model = User
        fields = ['username','email','password','admin_code']

    def create(self,validated_data):
        admin_code = validated_data.pop('admin_code')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        if admin_code == 'make-me-admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
        read_only_fields = ['username']
   
    def update(self, instance, validated_data):
        email = validated_data.get('email', instance.email)
        admin_code = validated_data.pop('admin_code',None)
        if admin_code == 'make-me-admin':
            instance.is_staff = True
            instance.is_superuser = True
        instance.email = email
        instance.save()
        return instance
    
class RegisterProfileSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = ['name','age','image','image_url']
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None

class ProfileSerializer(serializers.ModelSerializer):
    profile = RegisterProfileSerializer()
    class Meta:
        model = Profile
        feilds = ['name','age','image_url']