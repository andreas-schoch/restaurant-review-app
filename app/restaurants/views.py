from rest_framework.response import Response
from rest_framework import generics, status

from restaurants.serializers import RestaurantsSerializer
from rest_framework.generics import (ListCreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework.generics import get_object_or_404

from api.models import Restaurant


class GetAllRestaurantsView(ListCreateAPIView):
    """
    Class to GET  the list of all Restaurants or POST a new Restaurant
    """
    serializer_class = RestaurantsSerializer
    queryset = Restaurant.objects.all()
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = RestaurantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status 201": "Restaurant created succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetPostUpdateDeleteRestaurant(RetrieveUpdateDestroyAPIView):
    """
    Class to GET - PUT/PATCH (UPDATE) - DELETE: Restaurant by id
    """
    serializer_class = RestaurantsSerializer


    def get_object(self, pk):
        post = get_object_or_404(Restaurant, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = RestaurantsSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = RestaurantsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status 201": "Restaurant updated succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response({"Status 204": "Restaurant deleted succesfully"}, status=status.HTTP_204_NO_CONTENT)


class GetRestaurantByCategory(ListAPIView):
    """
    Class to GET all the restaurants by category
    """
    serializer_class = RestaurantsSerializer
    permission_classes = []
    authentication_classes = []

    def get_queryset(self):
        category = self.kwargs.get("category").title()
        return Restaurant.objects.filter(category=category)


class GetRestaurantByUserID(generics.ListAPIView):
    """
    Class to Get the all the restaurants owned (created) by a specific user in chronological order.
    """
    serializer_class = RestaurantsSerializer

    def get_queryset(self, *args, **kwargs):
        kwargs = self.kwargs  # --> a dictionary with the url's parameter {'author_id': '2'}
        kw_id = kwargs.get('user_id')  # --> returns the value of key='author_id'
        return Restaurant.objects.filter(restaurant_owner=kw_id)

