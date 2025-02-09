# Django Hotel

## 功能介紹
### 客人
- 訂房
- PayPal 支付訂金
- 查詢訂單
- 取消訂單
- 收到訂單通知信

### Django 後台
- 新增飯店
- 新增房號
- 查看訂單
- 串接 PayPal 支付

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Hotel
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
      PAYPAL_CLIENT_ID=your_paypal_client_id
      PAYPAL_CLIENT_SECRET=your_paypal_client_secret
      PAYPAL_MODE=sandbox
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
3. 訂房：
    - 訪問 `/book_room` 頁面，填寫訂房表單並提交。
4. 確認訂單：
    - 訪問 `/confirm_booking/<booking_id>` 頁面查看訂單詳情並支付訂金。
5. 支付訂金：
    - 訪問 `/process_payment/<booking_id>` 頁面進行 PayPal 支付。
6. 查詢訂單：
    - 訪問 `/search_booking` 頁面，輸入姓名和入住日期查詢訂單。
7. 取消訂單：
    - 訪問 `/cancel_booking/<booking_id>` 頁面取消訂單。
