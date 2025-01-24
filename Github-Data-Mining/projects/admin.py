from django.contrib import admin
from .models import Repository

# 註冊 Repository 模型到 Django 管理後台
admin.site.register(Repository)