from django.test import TestCase
from .models import Repository

# 定義測試用例來測試 Repository 模型
class RepositoryModelTest(TestCase):
    def setUp(self):
        Repository.objects.create(name="Test Repo", stars=100, language="Python", tech_stack="Django, DRF")

    def test_repository_creation(self):
        repo = Repository.objects.get(name="Test Repo")
        self.assertEqual(repo.stars, 100)
        self.assertEqual(repo.language, "Python")
        self.assertEqual(repo.tech_stack, "Django, DRF")