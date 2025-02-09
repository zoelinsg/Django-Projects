# Django Basic 1

## 功能介紹
- 使用者註冊
- 使用者登入
- 使用者登出
- 查看會員資料
- 修改會員資料

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Basic1
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
4. 查看和修改會員資料：
    - 登入後，訪問 `/profile` 頁面查看和修改個人資料。