from django_socio_grpc.services.app_handler_registry import AppHandlerRegistry
from credit_card.api.services import CreditCardService

def credit_card_grpc_handlers(server):
    app_registry = AppHandlerRegistry("credit_card", server)
    app_registry.register(CreditCardService)