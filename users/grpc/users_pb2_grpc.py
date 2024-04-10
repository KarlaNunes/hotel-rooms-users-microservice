# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from users.grpc import users_pb2 as users_dot_grpc_dot_users__pb2


class UserControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/Create',
                request_serializer=users_dot_grpc_dot_users__pb2.UserRequest.SerializeToString,
                response_deserializer=users_dot_grpc_dot_users__pb2.UserResponse.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/Destroy',
                request_serializer=users_dot_grpc_dot_users__pb2.UserDestroyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.List = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/List',
                request_serializer=users_dot_grpc_dot_users__pb2.UserListRequest.SerializeToString,
                response_deserializer=users_dot_grpc_dot_users__pb2.UserListResponse.FromString,
                )
        self.PartialUpdate = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/PartialUpdate',
                request_serializer=users_dot_grpc_dot_users__pb2.UserPartialUpdateRequest.SerializeToString,
                response_deserializer=users_dot_grpc_dot_users__pb2.UserResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/Retrieve',
                request_serializer=users_dot_grpc_dot_users__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=users_dot_grpc_dot_users__pb2.UserResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/hotel_rooms_users_services.users.UserController/Update',
                request_serializer=users_dot_grpc_dot_users__pb2.UserRequest.SerializeToString,
                response_deserializer=users_dot_grpc_dot_users__pb2.UserResponse.FromString,
                )


class UserControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PartialUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserRequest.FromString,
                    response_serializer=users_dot_grpc_dot_users__pb2.UserResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserDestroyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserListRequest.FromString,
                    response_serializer=users_dot_grpc_dot_users__pb2.UserListResponse.SerializeToString,
            ),
            'PartialUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.PartialUpdate,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserPartialUpdateRequest.FromString,
                    response_serializer=users_dot_grpc_dot_users__pb2.UserResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserRetrieveRequest.FromString,
                    response_serializer=users_dot_grpc_dot_users__pb2.UserResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=users_dot_grpc_dot_users__pb2.UserRequest.FromString,
                    response_serializer=users_dot_grpc_dot_users__pb2.UserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hotel_rooms_users_services.users.UserController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/Create',
            users_dot_grpc_dot_users__pb2.UserRequest.SerializeToString,
            users_dot_grpc_dot_users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/Destroy',
            users_dot_grpc_dot_users__pb2.UserDestroyRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/List',
            users_dot_grpc_dot_users__pb2.UserListRequest.SerializeToString,
            users_dot_grpc_dot_users__pb2.UserListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PartialUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/PartialUpdate',
            users_dot_grpc_dot_users__pb2.UserPartialUpdateRequest.SerializeToString,
            users_dot_grpc_dot_users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/Retrieve',
            users_dot_grpc_dot_users__pb2.UserRetrieveRequest.SerializeToString,
            users_dot_grpc_dot_users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hotel_rooms_users_services.users.UserController/Update',
            users_dot_grpc_dot_users__pb2.UserRequest.SerializeToString,
            users_dot_grpc_dot_users__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
