from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('project.api.auth.urls', namespace='auth')),
    path('registration/', include('project.api.registration.urls', namespace='registration')),
    path('feed/', include('project.api.feed.urls', namespace='feed')),
    path('users/', include('project.api.user.urls', namespace='user')),
    path('posts/', include('project.api.post.urls', namespace='post')),
    path('me/', include('project.api.me.urls', namespace='me')),
]
