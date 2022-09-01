from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    email = serializers.EmailField()
    tanggal_lahir = serializers.DateField()
    nama = serializers.CharField()