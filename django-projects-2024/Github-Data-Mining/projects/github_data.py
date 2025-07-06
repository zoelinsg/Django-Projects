import os
from github import Github
from dotenv import load_dotenv
from projects.models import Repository  # 使用絕對導入

# 加載 .env 文件中的環境變量
load_dotenv()

# 定義函數來從 GitHub 獲取熱門倉庫數據
def fetch_github_repositories():
    # 從環境變量中獲取 GitHub 存取令牌
    github_access_token = os.getenv('your_github_access_token')
    g = Github(github_access_token)
    
    # 搜索星數大於 1000 的倉庫
    repos = g.search_repositories(query='stars:>1000')
    
    # 更新或創建 Repository 模型實例
    for repo in repos[:10]:
        Repository.objects.update_or_create(
            name=repo.name,
            defaults={
                "stars": repo.stargazers_count,
                "language": repo.language,
                "tech_stack": ', '.join(repo.get_topics()),
            }
        )

# 執行函數來獲取數據
if __name__ == "__main__":
    fetch_github_repositories()