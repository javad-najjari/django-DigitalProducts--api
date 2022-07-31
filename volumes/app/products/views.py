from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from subscriptions.models import Subscription
from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer
from rest_framework.permissions import IsAuthenticated



class ProductListView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        if not Subscription.objects.filter(
            user = request.user,
            expire_time__gt = timezone.now()
        ).exists():
            return Response(status=status.HTTP_401_UNAUTHORIZED)
            
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)



class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)



class FileListView(APIView):

    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, product_id, pk):
        try:
            files = File.objects.get(pk=pk, product_id=product_id)
        except File.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FileSerializer(files, context={'request': request})
        return Response(serializer.data)

