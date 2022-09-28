from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from portfolio.serializers import ProjectSerializer, BlogPostSerializer
from portfolio.models import Project, BlogPost
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

# Create your views here.
class ProjectList(generics.ListAPIView):

    def get(self, request):
        data = self.get_queryset()
        serializer = ProjectSerializer(data, many=True)
        if len(serializer.data) != 0:
            return Response(data=serializer.data)
        else:
            return Response(data="No available projects", status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        query_set = Project.objects.filter(is_published=True)
        return query_set

        

class BlogPostList(generics.ListAPIView):
    def get(self, request):
        data = self.get_queryset()
        serializer = BlogPostSerializer(data, many=True)
        if len(serializer.data) != 0:
            return Response(data=serializer.data)
        else:
            return Response(data="No available Blogposts", status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        query_set = BlogPost.objects.filter(is_published=True)
        return query_set




class ProjectDetail(APIView):
    ''' Send project detail view from pk '''
    def get(self, request, pk):
        try:
            project = Project.objects.filter(is_published=True).get(pk=pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        except:
            return Response(data="Project not found", status=status.HTTP_400_BAD_REQUEST)


class BlogPostDetail(APIView):
    ''' Send blogpost detail view from pk '''
    def get(self, request, pk):
        try:
            project = BlogPost.objects.filter(is_published=True).get(pk=pk)
            serializer = BlogPostSerializer(project)
            return Response(serializer.data)
        except:
            return Response(data="Blogpost not found", status=status.HTTP_400_BAD_REQUEST)