from django_socio_grpc import proto_serializers
from users.models import User
from ..grpc.users_pb2 import (
    UserResponse,
    UserListResponse,
)


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "social_security_card")
        proto_class = UserResponse
        proto_class_list = UserListResponse