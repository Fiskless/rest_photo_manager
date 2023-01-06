from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Photo
from .serializers import PhotoCreateSerializer, PhotoWithoutMetaDataSerializer


class PhotoCreateView(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = PhotoWithoutMetaDataSerializer
    queryset = Photo.objects.all()

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

    def retrieve(self, request, *args, **kwargs):
        photo = self.get_object()
        serializer = PhotoCreateSerializer(photo)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)