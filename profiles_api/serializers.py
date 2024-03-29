from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    email = serializers.EmailField()
    tanggal_lahir = serializers.DateField()
    nama = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'nama', 'umur', 'tanggal_lahir', 'codeforces_id', 'password')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {'input_type' : 'password'}
            }
        }
    
    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            nama = validated_data['nama'],
            umur = validated_data['umur'],
            tanggal_lahir = validated_data['tanggal_lahir'],
            codeforces_id = validated_data['codeforces_id'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_tags', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}