from django.urls import path
from .views import GetUpdateUserProfileView

app_name = 'me'

urlpatterns = [
    path(
        '',
        GetUpdateUserProfileView.as_view(),
        name='get_update_user_profile'
    ),
]
