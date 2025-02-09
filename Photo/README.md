# Django Photos

## 功能介紹
### 帳號管理
- 註冊
- 登入
- 登出
- 個人資料查看
- 個人資料修改
- 忘記密碼
- 密碼驗證信
- 密碼修改
- 密碼重置

### 相簿管理
- 新增相簿
- 刪除相簿
- 修改相簿
- 查看相簿
- 查看相簿中相片

### 相片管理
- 新增相片
- 刪除相片
- 修改相片
- 查看相片

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Photo
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
    - 在專案根目錄下創建 `.env` 文件，並添加以下內容：
      ```properties
      YOUR_EMAIL_HOST_USER=your_email@example.com
      YOUR_EMAIL_HOST_PASSWORD=your_email_password
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
3. 新增相簿：
    - 登入後，訪問 `/album/add` 頁面，填寫相簿表單並提交。
4. 修改相簿：
    - 登入後，訪問 `/album/edit/<album_id>` 頁面，填寫相簿表單並提交。
5. 刪除相簿：
    - 登入後，訪問 `/album/delete/<album_id>` 頁面，確認刪除。
6. 查看相簿：
    - 訪問 `/album/<album_id>` 頁面查看相簿詳情。
7. 新增相片：
    - 登入後，訪問 `/photo/upload` 頁面，填寫相片表單並提交。
8. 修改相片：
    - 登入後，訪問 `/photo/edit/<photo_id>` 頁面，填寫相片表單並提交。
9. 刪除相片：
    - 登入後，訪問 `/photo/delete/<photo_id>` 頁面，確認刪除。
10. 查看相片：
    - 訪問 `/photo/<photo_id>` 頁面查看相片詳情。
