
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic, WishList
from django.contrib.auth.models import User

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers

class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()
    
    # def get_new_field(self, obj):
    #     return {'hola':10}

    class Meta:
        model = Comic
        fields = '__all__'
        # fields = ('marvel_id', 'title', 'new_field')
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('password',)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        fields = ('username', 'password')


# TODO: Realizar el serializador para el modelo de WishList
