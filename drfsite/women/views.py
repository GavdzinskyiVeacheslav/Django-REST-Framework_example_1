from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from rest_framework.pagination import PageNumberPagination


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class WomenAPIList(generics.ListCreateAPIView):
  queryset = Women.objects.all()
  serializer_class = WomenSerializer
  permission_classes = (IsAuthenticatedOrReadOnly,)
  pagination_class = WomenAPIListPagination

class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
  queryset = Women.objects.all()
  serializer_class = WomenSerializer
  permission_classes = (IsAuthenticated, )
  #authentication_class = (TokenAuthentication, )

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
  queryset = Women.objects.all()
  serializer_class = WomenSerializer
  permission_classes = (IsAdminOrReadOnly, )

# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     #queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#     def get_queryset(self):
#       pk = self.kwargs.get('pk')

#       if not pk:
#         return Women.objects.all()[:3]

#       return Women.objects.filter(pk=pk)

#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#       cats = Category.objects.get(pk=pk)
#       return Response({'cats': cats.name})



# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE not allowed'})

        # here is the code to delete the record with the transferred pk
        # serializer = Women.objects.get(pk=pk)
        # serializer.delete()
        #
        # return Response({'post': 'delete post ' + str(pk)})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
