from rest_framework import status, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response

from .filters import PhotoFilter
from .models import Photo
from .serializers import PhotoCreateSerializer, PhotoWithoutMetaDataSerializer
from django_filters import rest_framework as filters


class PhotoCreateView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    queryset = Photo.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PhotoFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoWithoutMetaDataSerializer
        else:
            return PhotoCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = PhotoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['people_names'] = [name.lstrip() for name in
                        serializer.validated_data['people_names'].split(',')]

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
