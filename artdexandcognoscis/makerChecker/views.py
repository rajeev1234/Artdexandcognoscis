from django.http import JsonResponse, request
from rest_framework import viewsets, permissions
from makerChecker.models import User,Make,Model,Variant
from makerChecker.serializers import UserSerializer,MakeSerializer,ModelSerializer,VariantSerializer,ViewAllVariantSerializer
from django.contrib.auth.hashers import make_password

from makerChecker.permissions import IsMaker,IsChecker,IsOwnerOrReadOnly
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)



class MakeViewSet(viewsets.ModelViewSet):
    queryset = Make.objects.all()
    serializer_class = MakeSerializer
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
        )

    def get_queryset(self):

        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ModelsViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
        )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer
    permission_classes = (
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,
        )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ViewAllVariantDetailViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Variant.objects.all()
            serializer = ViewAllVariantSerializer(queryset, many=True)
            return JsonResponse({'data' : serializer.data, 'message': 'success', 'status': 200})
        except Exception as ex:
            return JsonResponse({'message': str(ex), 'status': 400})