from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core.models import Address, Item, Order, OrderItem, Coupon, Variation, ItemVariation
from core.models import (
    Address, Item, Order, OrderItem, Coupon, Variation, ItemVariation,
    Payment
)


class StringSerializer(serializers.StringRelatedField):
@@ -195,3 +198,13 @@ class Meta:
            'address_type',
            'default'
        )


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id',
            'amount',
            'timestamp'
        )
