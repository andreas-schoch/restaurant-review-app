from django.apps import AppConfig


class FeedApp(AppConfig):
    name = 'project.feed'
    verbose_name = "Social feed app"

    def ready(self):
        from . import signals  # noqa
