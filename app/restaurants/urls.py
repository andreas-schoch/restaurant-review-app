from django.urls import path
from .views import (GetAllRestaurantsView,
                    GetPostUpdateDeleteRestaurantView,
                    GetRestaurantByCategoryView,
                    GetRestaurantByUserIDView)


urlpatterns = [
    path("", GetAllRestaurantsView.as_view(), name="get-list-of-all-restaurants"),
    path("category/<str:category>/", GetRestaurantByCategoryView.as_view(), name="get-restaurant-by-category"),
    path("<int:pk>/", GetPostUpdateDeleteRestaurantView.as_view(), name="get-post-delete-update-restaurant"),
    path("user/<int:user_id>/", GetRestaurantByUserIDView.as_view(), name="get-restaurants-by-user-id"),
]


