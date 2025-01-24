import os
from django.core.management.base import BaseCommand
from github import Github
from dotenv import load_dotenv
from projects.models import Repository

class Command(BaseCommand):
    help = 'Fetch GitHub repositories and save to database'

    def handle(self, *args, **kwargs):
        # 加載 .env 文件中的環境變量
        load_dotenv()

        # 從環境變量中獲取 GitHub 存取令牌
        github_access_token = os.getenv('your_github_access_token')
        g = Github(github_access_token)
        
        # 搜索星數大於 1000 的倉庫
        repos = g.search_repositories(query='stars:>800')
        
        # 更新或創建 Repository 模型實例
        for repo in repos[:10]:
            language = repo.language if repo.language else ''
            Repository.objects.update_or_create(
                name=repo.name,
                defaults={
                    "stars": repo.stargazers_count,
                    "language": language,
                    "tech_stack": ', '.join(repo.get_topics()),
                    "url": repo.html_url,  # 添加這行
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched and saved repositories'))