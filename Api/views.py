import logging

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import CatagoeryFilter
from .models import Catagoery
from .serializers import CatagoerySerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for user management. Anyone can create an account.
    Staff can view all users, while regular users can only view their own profile.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def get_queryset(self):
        try:
            user = self.request.user
            qs = super().get_queryset()
            if not user.is_staff:
                qs = qs.filter(username=user)
            return qs
        except Exception as e:
            logger.error(f"Error occure in get_queryset in UserViewSet: {e}")
            return User.objects.none()


class CatagoeryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing categories. Users can only view and
    manage their own categories.
    """

    queryset = Catagoery.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CatagoerySerializer
    filterset_class = CatagoeryFilter

    def get_queryset(self):
        try:
            user = self.request.user
            qs = super().get_queryset()
            qs = qs.filter(user=user)

            return qs
        except Exception as e:
            logger.error(f"Error occure in get_queryset in CatagoeryViewSet: {e}")
            return Catagoery.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
