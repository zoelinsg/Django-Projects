"""
Django 設定文件，用於 config 專案。

由 'django-admin startproject' 生成，使用 Django 5.1.5。

更多信息請參見
https://docs.djangoproject.com/en/5.1/topics/settings/

完整的設定列表及其值請參見
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# 在專案內部構建路徑，如： BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent


# 快速啟動開發設置 - 不適用於生產環境
# 請參見 https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# 安全警告：在生產環境中請保密使用的密鑰！
SECRET_KEY = 'django-insecure-x30f%!b@55*b4f@z_wv98*qx%nx!&%b-mn1zos_)nd0c1t()i#'

# 安全警告：不要在生產環境中開啟 debug！
DEBUG = True

ALLOWED_HOSTS = []


# 應用程序定義

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 確保包含 templates 路徑
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# 資料庫
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# 密碼驗證
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 國際化
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'zh-hant'  # 設定語言為繁體中文

TIME_ZONE = 'Asia/Taipei'  # 設定時區為台北

USE_I18N = True

USE_TZ = True


# 靜態文件 (CSS, JavaScript, 圖片)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # 假設 static 文件夾在專案根目錄
]
# 預設主鍵字段類型
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'