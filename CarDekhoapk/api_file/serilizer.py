from rest_framework import serializers
from CarDekhoapk.models import CarList

# Create a model serializer
class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = '__all__'
    def create(self, validated_data):
        return CarList.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.car_name = validated_data.get('car_name', instance.car_name)
        instance.car_price = validated_data.get('car_price', instance.car_price)
        instance.car_description = validated_data.get('car_description', instance.car_description)
        instance.car_color = validated_data.get('car_color', instance.car_color)
        instance.car_mileage= validated_data.get('car_mileage', instance.car_mileage)
        instance.active = validated_data.get('active', instance.active)
        instance.car_image= validated_data.get('car_image', instance.car_image)
        
        instance.save()
        return instance

