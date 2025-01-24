from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Repository
from .serializers import RepositorySerializer

# 定義 API 視圖來處理 Repository 的列表和詳細信息
class RepositoryList(APIView):
    def get(self, request):
        repos = Repository.objects.all()
        serializer = RepositorySerializer(repos, many=True)
        return Response(serializer.data)

# 定義視圖來渲染 Repository 列表的網頁
def repository_list_view(request):
    repos = Repository.objects.all()
    return render(request, 'repository_list.html', {'repositories': repos})

# 定義 API 視圖來處理 Repository 的詳細信息
class RepositoryDetail(APIView):
    def get(self, request, pk):
        try:
            repo = Repository.objects.get(pk=pk)
        except Repository.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RepositorySerializer(repo)
        return Response(serializer.data)

# 定義視圖來渲染 Repository 詳細信息的網頁
def repository_detail_view(request, pk):
    try:
        repo = Repository.objects.get(pk=pk)
    except Repository.DoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, 'repository_detail.html', {'repository': repo})

# 定義視圖來渲染首頁
def home_view(request):
    return render(request, 'index.html')

# 定義視圖來渲染 404 頁面
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)