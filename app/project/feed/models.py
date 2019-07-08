from django.conf import settings
from django.db import models

from project.api.helpers import code_generator


class Post(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
    )
    content = models.TextField(
        verbose_name='content'
    )
    created = models.DateTimeField(
        verbose_name='created',
        auto_now_add=True,
    )
    shared = models.ForeignKey(
        verbose_name='shared',
        to='self',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"{self.content[:50]} ..."

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']


class Like(models.Model):
    user = models.ForeignKey(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='likes',
        null=True,
    )
    post = models.ForeignKey(
        verbose_name='post',
        to='feed.Post',
        related_name='likes',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user} | {self.post}"

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        unique_together = [
            ('user', 'post'),
        ]


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
    )
    followees = models.ManyToManyField(
        verbose_name='following',
        to=settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True,
    )
    code = models.CharField(
        verbose_name='code',
        help_text='random code used for registration and for password reset',
        max_length=15,
        default=code_generator
    )

    def generate_new_code(self):
        self.code = code_generator()
        self.save()
        return self.code

    def __str__(self):
        return self.user.username


class FriendRequest(models.Model):
    DEFAULT_STATUS = 'pending'
    STATUS_CHOICES = [
        (DEFAULT_STATUS, 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    requester = models.ForeignKey(
        verbose_name='requester',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='connections',
    )
    receiver = models.ForeignKey(
        verbose_name='receiver',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='friend_requests',
    )
    status = models.CharField(
        verbose_name='status',
        choices=STATUS_CHOICES,
        default=DEFAULT_STATUS,
        max_length=100,
    )
