from rest_framework import serializers
from .models import Repository

# 定義序列化器來將 Repository 模型轉換為 JSON 格式
class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'