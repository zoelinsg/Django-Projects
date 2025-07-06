# Django Order

## 功能介紹
### 產品管理
- 查看產品
- 查看產品詳情
- 搜尋產品
- 依分類篩選產品

### 購物車管理
- 加入購物車
- 刪除購物車項目
- 修改購物車項目數量

### 訂單管理
- 選擇桌號
- 產生訂單
- 查看訂單狀態

### Django 後台
- 新增產品
- 修改產品
- 刪除產品
- 更改訂單狀態

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Order
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
1. 查看產品：
    - 訪問 `/menu` 頁面查看所有產品。
2. 查看產品詳情：
    - 訪問 `/menu/<product_id>` 頁面查看產品詳情。
3. 搜尋產品：
    - 使用搜尋框輸入關鍵字進行產品搜尋。
4. 加入購物車：
    - 在產品詳情頁面填寫數量並提交表單。
5. 查看購物車：
    - 訪問 `/cart` 頁面查看購物車內容。
6. 修改購物車項目數量：
    - 在購物車頁面修改數量並提交表單。
7. 刪除購物車項目：
    - 在購物車頁面點擊刪除按鈕。
8. 產生訂單：
    - 訪問 `/create_order` 頁面填寫訂單資訊並提交。
9. 查看訂單狀態：
    - 訪問 `/order/<order_id>` 頁面查看訂單詳情。
