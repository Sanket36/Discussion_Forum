from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
# Register your models here.
