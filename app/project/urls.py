from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

mypatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('project.api.urls', namespace='api')),
    path('docs/', include_docs_urls(title='Django social feed API', public=False))
]

urlpatterns = [
    path('backend/', include(mypatterns)),
]
