# 用戶模型和個人資料模型的定義
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# 定義用戶的個人資料模型，儲存用戶的額外資訊
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
        ('O', '其他'),
    ]  # 性別選項

    ROLE_CHOICES = [
        ('boss', '老闆'),
        ('employee', '員工'),
    ]  # 登入身分選項

    # 登入身分 老闆/員工
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # 連結到用戶模型的OneToOneField
    phone = models.CharField(max_length=15, blank=True)  # 電話欄位
    address = models.TextField(blank=True)  # 地址欄位
    birth_date = models.DateField(null=True, blank=True)  # 生日欄位
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)  # 性別欄位，使用選擇框
    website = models.URLField(blank=True)  # 個人網站欄位
    bio = models.TextField(blank=True)  # 簡介欄位
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')  # 登入身分欄位，預設為員工
    # 可根據需求添加更多個人資訊欄位

    def __str__(self):
        return self.user.username  # 返回用戶名作為模型的字串表示

# 當 User 被創建時自動創建 UserProfile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)  # 創建新用戶時，自動創建 UserProfile

# 當 User 儲存時也儲存對應的 UserProfile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # 儲存 User 時，自動儲存對應的 UserProfile