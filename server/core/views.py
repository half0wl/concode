from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from core.models import Project
from core.serializers import UserSerializer, ProjectSerializer
from core.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):

    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user,
                                         data=request.data,
                                         partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ProjectList(generics.ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def create(self, request, **kwargs):
        data = {
            'owner': request.user.id,
            'name': request.data['name'],
            'description': request.data['description'],
            'stage': request.data['stage'],
        }
        serializer = self.get_serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
