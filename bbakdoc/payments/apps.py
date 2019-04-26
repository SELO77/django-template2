from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    name = "bbakdoc.payments"
    verbose_name = "Payments"

    def ready(self):
        pass
        # try:
        #     import users.signals  # noqa F401
        # except ImportError:
        #     pass
