from django_socio_grpc import generics

from credit_card.models import CreditCard
from .serializers import CreditCardProtoSerializer

class CreditCardService(generics.ModelService):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardProtoSerializer