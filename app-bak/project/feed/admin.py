from django.contrib import admin

from project.feed.models import Post, Like, FriendRequest, UserProfile

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(FriendRequest)
admin.site.register(UserProfile)
