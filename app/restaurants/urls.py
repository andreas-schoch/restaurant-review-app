from django.urls import path
from .views import (GetAllRestaurantsView,
                    GetPostUpdateDeleteRestaurant,
                    GetRestaurantByCategory,
                    GetRestaurantByUserID)


urlpatterns = [
    path("", GetAllRestaurantsView.as_view(), name="get-list-of-all-restaurants"),
    path("category/<str:category>/", GetRestaurantByCategory.as_view(), name="get-restaurant-by-category"),
    path("<int:pk>/", GetPostUpdateDeleteRestaurant.as_view(), name="get-post-delete-update-restaurant"),
    path("user/<int:user_id>/", GetRestaurantByUserID.as_view(), name="get-restaurants-by-user-id"),
]


