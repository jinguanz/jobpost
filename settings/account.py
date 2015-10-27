__author__ = 'jinguangzhou'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'account',
        'USER': 'root',
        # 'PASSWORD': 'zjg',
    }
}
AUTH_USER_MODEL = 'account.MyUser'
