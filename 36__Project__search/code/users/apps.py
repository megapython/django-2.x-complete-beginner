from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # signal is called as soon as registry is populated
    def ready(self):
        import users.signals
