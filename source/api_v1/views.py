from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions

# from api_v1.serializers import QuoteSerializer, QuoteUpdateSerializer, QuoteRatingSerializer
# from webapp.models import Quote, QUOTE_APPROVED


# class IsPostOrIsAuthenticated(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         # allow all POST requests
#         if request.method == 'POST':
#             return True
#         # Otherwise, only allow authenticated requests
#         return request.user and request.user.is_authenticated
from api_v1.serializers import CommentSerializer, LikeSerializer
from webapp.models import Like, Comment, Photo


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
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
