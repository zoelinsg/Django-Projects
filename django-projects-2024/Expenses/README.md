# Django Expenses

## 功能介紹
- 帳號管理：註冊、登入、登出、查看個人資料、修改個人資料
- 密碼管理：忘記密碼、密碼驗證信、修改密碼、密碼重置
- 帳戶管理：新增、刪除、修改、查看、查看帳戶記帳項目、轉帳
- 記帳管理：新增、刪除、修改、查看、依日期篩選、依類別篩選、轉帳紀錄

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Expenses
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
4. 查看個人資料：
    - 登入後，訪問 `/profile` 頁面查看和修改個人資料。
5. 忘記密碼：
    - 訪問 `/password_reset` 頁面，輸入註冊郵箱並提交。
6. 密碼重置：
    - 根據郵件中的連結，訪問密碼重置頁面，輸入新密碼並提交。
7. 新增帳戶：
    - 訪問 `/account/create` 頁面，填寫表單並提交。
8. 修改帳戶：
    - 訪問 `/account/edit/<id>` 頁面，填寫表單並提交。
9. 刪除帳戶：
    - 訪問 `/account/delete/<id>` 頁面，確認刪除。
10. 查看帳戶記帳項目：
    - 訪問 `/account/<id>/expenses` 頁面查看特定帳戶的記帳項目。
11. 新增記帳項目：
    - 訪問 `/expense/create` 頁面，填寫表單並提交。
12. 修改記帳項目：
    - 訪問 `/expense/edit/<id>` 頁面，填寫表單並提交。
13. 刪除記帳項目：
    - 訪問 `/expense/delete/<id>` 頁面，確認刪除。
14. 依日期篩選記帳項目：
    - 訪問 `/expense/filter_by_date` 頁面，選擇日期範圍並提交。
15. 依類別篩選記帳項目：
    - 訪問 `/expense/filter_by_category` 頁面，選擇類別並提交。
16. 轉帳：
    - 訪問 `/transfer` 頁面，填寫轉帳表單並提交。