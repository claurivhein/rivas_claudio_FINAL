from rest_framework import serializers
from .models import Inscritos, Institucion, DatosAutor

class InscritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class DatosAutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosAutor
        fields = '__all__'