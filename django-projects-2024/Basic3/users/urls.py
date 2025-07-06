from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    CustomPasswordChangeView, CustomPasswordChangeDoneView, CustomPasswordResetDoneView,
    CustomPasswordResetView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView,
    dashboard, register_user, user_profile_view, boss_dashboard, employee_dashboard, home
)

urlpatterns = [
    path('', dashboard, name='dashboard'),  # 首頁
    path('home/', home, name='home'),  # 首頁
    path('accounts/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # 登出
    path('register/', register_user, name='register'),  # 註冊
    path('profile/', user_profile_view, name='user-profile'),  # 個人資料
    path('boss_dashboard/', boss_dashboard, name='boss_dashboard'),  # 老闆儀表板
    path('employee_dashboard/', employee_dashboard, name='employee_dashboard'),  # 員工儀表板
    
    # 忘記密碼功能的 URL 路由
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),  # 忘記密碼
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),  # 忘記密碼郵件發送成功
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # 重設密碼確認
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),  # 重設密碼完成

    # 修改密碼功能的 URL 路由
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),  # 修改密碼
    path('password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),  # 修改密碼成功
]