from django.db import models

# 定義 Repository 模型來存儲 GitHub 倉庫數據
class Repository(models.Model):
    name = models.CharField(max_length=255)
    stars = models.IntegerField()
    language = models.CharField(max_length=50)
    tech_stack = models.TextField()
    url = models.URLField(max_length=200)  # 添加這行
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name