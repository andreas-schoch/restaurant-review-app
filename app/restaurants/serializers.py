from rest_framework import serializers
from api.models import Restaurant


class RestaurantsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'category', 'street', 'city', 'zip', 'website', 'phone']
        read_only_fields = ['id']

        # name = models.CharField(blank=False, null=False, max_length=15)
        # category = models.CharField(
        #     blank=False, null=False,
        #     max_length=15,
        #     choices=CATEGORY_CHOICES
        # )
        # country = models.CharField(blank=False, null=False, max_length=30)
        # street = models.CharField(blank=False, null=False, max_length=30)
        # city = models.CharField(blank=False, null=False, max_length=30)
        # zip = models.CharField(null=True, blank=True, max_length=30)
        # website = models.CharField(null=True, blank=True, max_length=30)
        # phone = models.CharField(null=True, blank=True, max_length=30)
        # email = models.CharField(null=True, blank=True, max_length=30)
        # opening_hours = models.CharField(null=True, blank=True, max_length=30)
        # price_level = models.IntegerField(null=True, blank=True)
        # restaurant_pic = models.ImageField(null=True, blank=True, max_length=30)