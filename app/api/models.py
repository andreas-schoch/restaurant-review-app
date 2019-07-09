from django.contrib.auth import get_user_model
from django.db import models
# from app_api.helpers import code_generator

User = get_user_model()

CATEGORY_CHOICES = (('Asian', 'Asian'), ('Italian', 'Italian'),
                    ('Swiss', 'Swiss'), ('Greek', 'Greek'),)


class UserProfile(models.Model):
    user = models.OneToOneField(
        verbose_name='user',
        to=User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    location = models.CharField(null=True, blank=True, max_length=30)
    phone = models.CharField(null=True, blank=True, max_length=30)
    bio = models.CharField(max_length=300, blank=True)
    interests = models.CharField(null=True, blank=True, max_length=30)
    profile_pic = models.ImageField(null=True, blank=True)
    # code = models.CharField(
    #     verbose_name='code',
    #     help_text='random code used for registration and for password reset',
    #     max_length=15,
    #     default=code_generator,
    #     null=True,
    #     blank=True
    # )

    def __str__(self):
        return self.user.username


class Restaurant(models.Model):

    name = models.CharField(blank=False, null=False, max_length=15)
    category = models.CharField(
        blank=False, null=False,
        max_length=15,
        choices=CATEGORY_CHOICES
    )
    country = models.CharField(blank=False, null=False, max_length=30)
    street = models.CharField(blank=False, null=False, max_length=30)
    city = models.CharField(blank=False, null=False, max_length=30)
    zip = models.CharField(null=True, blank=True, max_length=30)
    website = models.CharField(null=True, blank=True, max_length=30)
    phone = models.CharField(null=True, blank=True, max_length=30)
    email = models.CharField(null=True, blank=True, max_length=30)
    opening_hours = models.CharField(null=True, blank=True, max_length=30)
    price_level = models.IntegerField(null=True, blank=True)
    restaurant_pic = models.ImageField(null=True, blank=True, max_length=30)

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(
        to=User,
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='authors'
    )
    restaurant = models.ForeignKey(
        to=Restaurant,
        verbose_name='Restaurant',
        on_delete=models.CASCADE,
        related_name='restaurants'
    )
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    # likes = models.IntegerField()

    def __str__(self):
        return f"{str(self.author).upper()}'s Comment for {str(self.restaurant).upper()}"


class Reaction(models.Model):
    class Meta:
        unique_together = (('user_reacted', 'comment'),)

    user_reacted = models.ForeignKey(
        to=User,
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='users_reacted')
    comment = models.ForeignKey(
        to=Comment,
        verbose_name='Comment',
        on_delete=models.CASCADE,
        related_name='comments')

    def __str__(self):
        return f"Liked: {self.comment}"


class Ownership(models.Model):
    class Meta:
        unique_together = (('owner', 'restaurant'),)

    owner = models.ForeignKey(
        to=User,
        verbose_name='Owner',
        on_delete=models.CASCADE,
        related_name='owners'
    )
    restaurant = models.ForeignKey(
        to=Restaurant,
        verbose_name='Restaurant',
        on_delete=models.CASCADE,
        related_name='owner_restaurants'
    )

    def __str__(self):
        return f"{str(self.owner).upper()} is the Owner of {str(self.restaurant).upper()}!"
