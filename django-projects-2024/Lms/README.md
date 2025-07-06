# Django LMS

## 功能介紹
### 帳號管理
- 註冊
- 登入
- 登出
- 忘記密碼
- 密碼驗證信
- 密碼重置
- 密碼修改

### 權限管理
- 分老師和學生管理權限
- 儀表板

### 課程管理
- 新增課程
- 刪除課程
- 修改課程
- 查看課程
- 選修課程
- 退選課程
- 查看選修名單

### 作業管理
- 新增作業
- 刪除作業
- 修改作業
- 查看作業
- 繳交作業
- 批改作業

### 考試管理
- 新增考試
- 刪除考試
- 修改考試
- 編輯考題
- 查看考試
- 學生考試

### 成績管理
- 作業成績
- 考試成績
- 課程總成績
- 管理課程成績

## 安裝與設定
1. 確認已安裝 [Poetry](https://python-poetry.org/)
2. 克隆此專案到本地端：
    ```bash
    git clone https://github.com/zoelinsg/Django-Projects.git
    ```
3. 進入專案目錄：
    ```bash
    cd Lms
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
3. 新增課程：
    - 老師登入後，訪問 `/add_course` 頁面，填寫課程表單並提交。
4. 修改課程：
    - 老師登入後，訪問 `/edit_course/<course_id>` 頁面，填寫課程表單並提交。
5. 刪除課程：
    - 老師登入後，訪問 `/delete_course/<course_id>` 頁面，確認刪除。
6. 新增作業：
    - 老師登入後，訪問 `/assignment_create` 頁面，填寫作業表單並提交。
7. 修改作業：
    - 老師登入後，訪問 `/assignment_update/<pk>` 頁面，填寫作業表單並提交。
8. 刪除作業：
    - 老師登入後，訪問 `/assignment_delete/<pk>` 頁面，確認刪除。
9. 學生繳交作業：
    - 學生登入後，訪問 `/submission_create/<assignment_pk>` 頁面，填寫繳交表單並提交。
10. 老師批改作業：
    - 老師登入後，訪問 `/grade_submission/<submission_pk>` 頁面，填寫成績表單並提交。
11. 新增考試：
    - 老師登入後，訪問 `/exam_create` 頁面，填寫考試表單並提交。
12. 修改考試：
    - 老師登入後，訪問 `/exam_update/<pk>` 頁面，填寫考試表單並提交。
13. 刪除考試：
    - 老師登入後，訪問 `/exam_delete/<pk>` 頁面，確認刪除。
14. 學生進行考試：
    - 學生登入後，訪問 `/take_exam/<exam_pk>` 頁面，填寫考試表單並提交。
15. 查看成績：
    - 學生登入後，訪問 `/total_grades` 頁面查看總成績。
