from django.urls import path
from .views import (GetAllRestaurantsView,
                    GetPostDeleteRestaurant)


urlpatterns = [
    path("", GetAllRestaurantsView.as_view(), name="get-list-of-all-restaurants"),
    path("new/", CreateNewRestaurantView.as_view(), name="create-new-restaurant"),
    # path("restaurants/category/<str:category>/", GetRestaurantByOwnerID.as_view(), name="get-restaurant-by-owner-id"),
    # path("restaurants/user/<int:user_id>/", GetRestaurantByUserID.as_view(), name="get-restaurants-by-user-id"),
    # path("restaurants/<int:pk>/", GetPostDeleteRestaurant.as_view(), name="get-post-delete-restaurant"),

]


