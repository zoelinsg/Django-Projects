# Django CRM

## 功能介紹
- 使用者註冊
- 使用者登入
- 使用者登出
- 查看客戶資料
- 新增客戶資料
- 修改客戶資料
- 刪除客戶資料

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd CRM
    ```
4. 使用 Poetry 安裝依賴：
    ```bash
    poetry install
    ```
5. 建立並啟動虛擬環境：
    ```bash
    poetry shell
    ```
6. 進行資料庫遷移：
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7. 創建超級用戶：
    ```bash
    python manage.py createsuperuser
    ```
8. 啟動開發伺服器：
    ```bash
    python manage.py runserver
    ```

## 使用說明
1. 註冊新帳號：
    - 訪問 `/register` 頁面，填寫註冊表單並提交。
2. 登入：
    - 訪問 `/login` 頁面，輸入帳號和密碼並提交。
3. 登出：
    - 點擊頁面上的登出按鈕。
4. 查看客戶資料：
    - 登入後，訪問 `/record/<id>` 頁面查看特定客戶資料。
5. 新增客戶資料：
    - 登入後，訪問 `/add_record` 頁面，填寫表單並提交。
6. 修改客戶資料：
    - 登入後，訪問 `/update_record/<id>` 頁面，填寫表單並提交。
7. 刪除客戶資料：
    - 登入後，訪問 `/delete_record/<id>` 頁面，確認刪除。
