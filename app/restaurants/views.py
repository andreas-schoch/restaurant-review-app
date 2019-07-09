# from rest_framework.generics import (ListAPIView,
#                                      CreateAPIView,
#                                      DestroyAPIView,
#                                      RetrieveUpdateDestroyAPIView)

# from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from api.models import Comment
from comments.serializers import CommentsSerializer
from restaurants.serializers import RestaurantsSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Restaurant


class GetAllRestaurantsView(ListCreateAPIView):
    """
    Class to GET the list of all restaurants or POST a new restaurant
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


class GetPostDeleteRestaurant(RetrieveUpdateDestroyAPIView):
    """
    GET - PUT/PATCH (UPDATE) - DELETE: Restaurant by id
    """
    permission_classes = (RestaurantPatchDeletePutPermission,)
    serializer_class = RestaurantsSerializer
    queryset = Restaurant.objects.all()
#
#
# # GET: Get the all the restaurants created by a specific user in chronological order.
# class GetRestaurantByUserID(ListAPIView):
#     serializer_class = RestaurantsSerializer
#     permission_classes = []
#     authentication_classes = []
#
#     def get_queryset(self):
#         user_id = self.kwargs.get("user_id")
#         return Restaurant.objects.filter(restaurant_owner=user_id).order_by("-created")
#
#
# # GET: Get the all the restaurants by category.
# class GetRestaurantByOwnerID(ListAPIView):
#     serializer_class = RestaurantsSerializer
#     permission_classes = []
#     authentication_classes = []
#
#     def get_queryset(self):
#         category = self.kwargs.get("category").title()
#         return Restaurant.objects.filter(category=category)
#
# class CommentCreateAPIView(APIView):
#     """
#     Class to POST a Comment
#     """
#
#     def get(self, request):
#         comment = Comment.objects.first()
#         serializer = CommentsSerializer(comment)
#         return Response({"This is a typical Json post": {"required": "title, body, author"}, "data": serializer.data})
#
#     def post(self, request):
#         serializer = CommentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Status 201": "Post created succesfully"},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
