from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
    AppSerializer,
    PlanSerializer,
    SubscriptionSerializer
)

from apps.models import (
    App,
    Plan,
    Subscription
)

class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class AppViewset(ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes= (IsAuthenticated,)

    def get_queryset(self):
        return App.objects.filter(user=self.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.user)



class PlanViewset(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes= (IsAuthenticated,)

class SubscriptionViewset(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes= (IsAuthenticated,)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.user)