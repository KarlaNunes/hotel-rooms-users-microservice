from django_socio_grpc import generics

from users.models import User
from .serializers import UserProtoSerializer


class UserService(generics.ModelService):
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer