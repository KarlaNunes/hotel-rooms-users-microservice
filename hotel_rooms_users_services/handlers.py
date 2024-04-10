from users.handlers import user_grpc_handlers
from credit_card.handlers import credit_card_grpc_handlers

def grpc_handlers(server):
    user_grpc_handlers(server)
    credit_card_grpc_handlers(server)
