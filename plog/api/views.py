from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from blogs.models import Blog
from api.serializers import BlogSerializer
from django.views.decorators.csrf import csrf_exempt

# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
# 
# @api_view(['GET', 'POST'])
# def blog_details(request, pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
# 
#     if request.method == 'GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
# 
#     return Response(status=status.HTTP_404_NOT_FOUND)
    
