from rest_framework import serializers

from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """
        Serializer para POST y PUT

        Ejemplo de JSON a enviar en POST / PUT:
            {
                "user": 3,
                "movie": 5,
                "content": "Me encantó la película"
            }
    """
    class Meta:
        model = Review
        fields = '__all__'

class ReviewDetailSerializer(serializers.ModelSerializer):
    """
        Serializer para GET (Listar detalles)

        Ejemplo de respuesta JSON:

            {
            "id": 2,
            "user": "heverrubio",
            "content": "Animación increíble!",
            "created_at": "2023-05-06T12:43:02.955166-06:00",
            "last_updated": "2023-05-06T12:43:02.955207-06:00",
            "movie": {
            "id": 5,
            "name": "Gato con botas: el último deseo",
            "year": 2022,
            "synopsis": "El Gato con Botas descubre que, debido a su pasión por la aventura, ha gastado ya 8 de sus 9 vidas. Por tanto, emprende un peligroso viaje en busca del legendario Último Deseo para solicitar que le restauren las vidas que ya perdió."
            }
            }
    """
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1