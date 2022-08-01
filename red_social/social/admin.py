from django.contrib import admin
from .models import Post,Profile

# Register your models here.

admin.site.register(Profile)  # registra la tabla para que se pueda ver desde el sitio de administración de django
admin.site.register(Post)

