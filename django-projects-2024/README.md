# Django-Projects
這個倉庫包含了多個基於 Django 和 Django REST framework 的專案，展示了如何構建 RESTful API 以及各種功能模組的實現。

## 專案列表
- **Basic1**：使用者註冊、登入、登出、查看和修改會員資料
- **Basic2**：使用者註冊、登入、登出、查看和修改會員資料、忘記密碼、密碼重置
- **Basic3**：使用者註冊、登入、登出、查看和修改會員資料、忘記密碼、密碼重置、不同身分登入後導向不同頁面
- **CRM**：客戶資料管理、訂單管理、報表生成
- **Expenses**：帳戶管理、記帳管理、報表生成
- **Github Data Mining**：使用 GitHub API 爬取熱門倉庫數據，並展示詳細信息
- **Hotel**：訂房、支付訂金、查詢和取消訂單、管理飯店和房號
- **LMS**：課程管理、作業管理、考試管理、成績管理
- **Order**：產品管理、購物車管理、訂單管理、支付管理
- **Photos**：相簿管理、相片管理
- **PIXBlog**：使用 PIXNET 痞客幫的 Open Data API 顯示國內旅遊的部落格文章
- **Store**：產品管理、購物車管理、訂單管理、支付管理

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此倉庫到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd <project-name>
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
    - 在專案根目錄下創建 `.env` 文件，並添加必要的環境變數。
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
