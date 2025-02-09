# 開源專案數據挖掘平臺

開源專案數據挖掘平臺是一個基於 Django 和 GitHub API 的應用，旨在爬取和展示 GitHub 上的熱門開源倉庫數據。用戶可以查看倉庫的詳細信息，包括星數、語言、技術棧等，並提供按技術、語言或熱度的篩選功能。

## 功能說明
- **首頁**: 展示平台簡介和功能介紹。
- **倉庫列表**: 顯示從 GitHub 獲取的熱門倉庫列表，包括倉庫名稱、星數和語言。
- **倉庫詳情**: 顯示選定倉庫的詳細信息，包括星數、語言、技術棧和 GitHub 連結。
- **數據更新**: 通過自定義管理命令從 GitHub 獲取最新的倉庫數據並保存到數據庫中。

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Github-Data-Mining
    ```
4. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```
5. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```
6. 設定環境變數：
    - 在專案根目錄下創建 `.env` 文件，並添加 GitHub 存取令牌：
      ```
      ithubyour_g_access_token=YOUR_GITHUB_ACCESS_TOKEN
      ```
7. 進行資料庫遷移：
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
8. 創建超級用戶：
    ```bash
    python manage.py createsuperuser
    ```
9. 啟動開發伺服器：
    ```bash
    python manage.py runserver
    ```

## 使用說明
1. 註冊新帳號：
    - 訪問 `/register` 頁面，填寫註冊表單並提交。
2. 登入：
    - 訪問 `/login` 頁面，輸入帳號和密碼並提交。
3. 查看倉庫列表：
    - 訪問 `/repositories` 頁面查看熱門倉庫列表。
4. 查看倉庫詳情：
    - 訪問 `/repositories/<id>` 頁面查看特定倉庫的詳細信息。
5. 更新數據：
    - 執行自定義管理命令來從 GitHub 獲取最新數據並更新數據庫：
      ```bash
      python manage.py fetch_github_data
      ```
