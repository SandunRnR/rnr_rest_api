from rest_framework import serializers
from .models import ProductForecastStage
from forecast_products.models import Product

class ProductForecastStageSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(source='product.product_id')

    class Meta:
        model = ProductForecastStage
        fields = [
            'id', 
            'product_id', 
            'operation_number', 
            'operation', 
            'resident', 
            'duration', 
            'start_date', 
            'end_date', 
            'production_order_number', 
            'production_order_type'
        ]

    def create(self, validated_data):
        product_id = validated_data.pop('product')['product_id']
        product = Product.objects.get(product_id=product_id)
        operation_number = ProductForecastStage.objects.create(product=product, **validated_data)
        return operation_number

    def update(self, instance, validated_data):
        product_id = validated_data.pop('product')['product_id']
        product = Product.objects.get(product_id=product_id)
        instance.product = product
        instance.operation_number = validated_data.get('operation_number', instance.operation_number)
        instance.operation = validated_data.get('operation', instance.operation)
        instance.resident = validated_data.get('resident', instance.resident)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.production_order_number = validated_data.get('production_order_number', instance.production_order_number)
        instance.production_order_type = validated_data.get('production_order_type', instance.production_order_type)
        instance.save()
        return instance
