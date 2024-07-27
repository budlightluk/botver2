from django.contrib import admin
from .models import TelegramUser, Project, Task

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

admin.site.register(TelegramUser)
admin.site.register(Project)
admin.site.register(Task)
