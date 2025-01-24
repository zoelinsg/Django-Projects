from django.urls import path
from .views import RepositoryList, RepositoryDetail, repository_list_view, repository_detail_view

urlpatterns = [
    # API 路由
    path('repositories/', RepositoryList.as_view(), name='repository-list'),
    path('repositories/<int:pk>/', RepositoryDetail.as_view(), name='repository-detail'),
    
    # 網頁視圖路由
    path('repositories/view/', repository_list_view, name='repository-list-view'),
    path('repositories/view/<int:pk>/', repository_detail_view, name='repository-detail-view'),
]