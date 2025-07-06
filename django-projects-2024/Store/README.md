# Django Store

## 功能介紹
### 帳號管理
- 註冊
- 登入
- 登出
- 忘記密碼
- 密碼驗證信
- 密碼重置
- 密碼修改
- 個人資料查看
- 個人資料修改

### 產品管理
- 查看所有產品列表
- 查看產品詳情
- 搜尋產品
- 查看分類產品

### 購物車管理
- 將商品加入購物車
- 修改購物車購買數量
- 刪除購物車商品項目
- 訂單確認明細

### 訂單管理
- 送出訂單
- 查看我的訂單
- 查看訂單詳情
- 確認訂單
- 取消訂單

### 支付管理
- PayPal 支付

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Store
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
      PAYPAL_CLIENT_ID=your_paypal_client_id
      PAYPAL_CLIENT_SECRET=your_paypal_client_secret
      PAYPAL_MODE=sandbox
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
3. 查看產品：
    - 訪問 `/products` 頁面查看所有產品。
4. 查看產品詳情：
    - 訪問 `/products/<product_id>` 頁面查看產品詳情。
5. 搜尋產品：
    - 使用搜尋框輸入關鍵字進行產品搜尋。
6. 加入購物車：
    - 在產品詳情頁面填寫數量並提交表單。
7. 查看購物車：
    - 訪問 `/cart` 頁面查看購物車內容。
8. 修改購物車項目數量：
    - 在購物車頁面修改數量並提交表單。
9. 刪除購物車項目：
    - 在購物車頁面點擊刪除按鈕。
10. 送出訂單：
    - 訪問 `/create_order` 頁面填寫訂單資訊並提交。
11. 查看訂單狀態：
    - 訪問 `/order/<order_id>` 頁面查看訂單詳情。
12. 確認訂單：
    - 訪問 `/confirm_order/<order_id>` 頁面確認訂單。
13. 取消訂單：
    - 訪問 `/cancel_order/<order_id>` 頁面取消訂單。
14. 支付訂單：
    - 訪問 `/process_payment/<order_id>` 頁面進行 PayPal 支付。
