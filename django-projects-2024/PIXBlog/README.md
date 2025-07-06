# Django PIXBlog

## 使用 PIXNET 痞客幫的 Open Data API，來顯示國內旅遊的部落格文章

## 參考教程
(https://www.learncodewithmike.com/2020/03/django-bootstrap.html)

## 功能介紹
- 顯示國內旅遊的熱門部落格文章

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd PIXBlog
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
1. 訪問首頁：
    - 啟動開發伺服器後，訪問 `http://localhost:8000` 查看國內旅遊的熱門部落格文章。
