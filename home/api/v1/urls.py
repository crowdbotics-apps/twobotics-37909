from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    AppViewset,
    PlanViewset,
    SubscriptionViewset
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("apps", AppViewset, basename="apps")
router.register("plans", PlanViewset, basename="plans")
router.register("subscriptions", SubscriptionViewset, basename="subscriptions")

urlpatterns = [
    path("", include(router.urls)),
]
