from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from users.api.services import UserService

def grpc_handlers(server):
    app_registry = AppHandlerRegistry("users", server)
    app_registry.register(UserService)