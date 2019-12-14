from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny, SAFE_METHODS, IsAuthenticated, \
    DjangoModelPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from api_v1.serializers import CommentSerializer, LikeSerializer
from webapp.models import Like, Comment, Photo


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        else:
            return [DjangoModelPermissions()]


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        pk = request.data.get('photo')
        photo = Photo.objects.get(pk=pk)
        if self.queryset.filter(photo=photo):
            return Response({'error': 'You already liked this photo'}, status=400)
        photo.likes += 1
        photo.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pk = request.data.get('photo')
        photo = Photo.objects.get(pk=pk)
        if not self.queryset.filter(photo=photo):
            return Response({'error': 'Nothing to unlike yet!'}, status=400)
        photo.likenum -= 1
        photo.save()
        return super(LikeViewSet, self).create(request, *args, **kwargs)