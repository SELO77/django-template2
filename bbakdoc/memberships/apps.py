from django.apps import AppConfig


class MembershipsConfig(AppConfig):
    name = "bbakdoc.memberships"
    verbose_name = "Memberships"

    def ready(self):
        pass
        # try:
        #     import users.signals  # noqa F401
        # except ImportError:
        #     pass
