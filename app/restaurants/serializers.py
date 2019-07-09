from rest_framework import serializers
from api.models import Restaurant


class RestaurantsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_owner', 'name', 'category', 'country', 'street', 'city',
                  'zip', 'website', 'phone', 'opening_hours', 'price_level', 'restaurant_pic']
        read_only_fields = ['id']


