from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "Users"

    def ready(self) -> None:
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
