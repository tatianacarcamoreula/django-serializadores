
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic

# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers


class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()

    # def get_new_field(self, obj):
    #     return {'message': 'Acá puedo devolver más información.'}

    class Meta:
        model = Comic
        fields = '__all__'
        # fields = ('marvel_id', 'title', 'new_field')
        read_only_fields = ('id',)
