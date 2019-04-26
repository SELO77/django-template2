from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = "bbakdoc.events"
    verbose_name = "Events"

    def ready(self):
        pass
        # try:
        #     import users.signals  # noqa F401
        # except ImportError:
        #     pass
