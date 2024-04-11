from django_socio_grpc import proto_serializers
from credit_card.models import CreditCard

from ..grpc.credit_card_pb2 import (
    CreditCardResponse,
    CreditCardListResponse,
)


class CreditCardProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = CreditCard
        fields = ("id", "number", "due_date", "owner", "cvv")
        proto_class = CreditCardResponse
        proto_class_list = CreditCardListResponse