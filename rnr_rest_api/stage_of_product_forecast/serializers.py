from rest_framework import serializers
from .models import ProductForecastStage
from forecast_products.models import Product

class ProductForecastStageSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(source='product.product_id')

    class Meta:
        model = ProductForecastStage
        fields = ['id', 'product_id', 'stage_of_product', 'start_date', 'end_date']

    def create(self, validated_data):
        product_id = validated_data.pop('product')['product_id']
        product = Product.objects.get(product_id=product_id)
        product_forecast_stage = ProductForecastStage.objects.create(product=product, **validated_data)
        return product_forecast_stage

    def update(self, instance, validated_data):
        product_id = validated_data.pop('product')['product_id']
        product = Product.objects.get(product_id=product_id)
        instance.product = product
        instance.stage_of_product = validated_data.get('stage_of_product', instance.stage_of_product)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance
