from users.handlers import user_grpc_handlers


def grpc_handlers(server):
    user_grpc_handlers(server)
