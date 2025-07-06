# Django Basic 3

## 功能介紹
- 使用者註冊
- 使用者登入
- 使用者登出
- 查看會員資料
- 修改會員資料
- 忘記密碼
- 忘記密碼郵件
- 密碼重置
- 不同身分登入後導向不同頁面

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Basic3
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
3. 登出：
    - 點擊頁面上的登出按鈕。
4. 查看和修改會員資料：
    - 登入後，訪問 `/profile` 頁面查看和修改個人資料。
5. 忘記密碼：
    - 訪問 `/password_reset` 頁面，輸入註冊郵箱並提交。
6. 密碼重置：
    - 根據郵件中的連結，訪問密碼重置頁面，輸入新密碼並提交。
7. 不同身分登入後導向不同頁面：
    - 老闆登入後導向 `/boss_dashboard` 頁面。
    - 員工登入後導向 `/employee_dashboard` 頁面。