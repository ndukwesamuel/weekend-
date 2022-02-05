from django.contrib import admin

# Register your models here.
from Home.models import Post, PRoduct, Profile

admin.site.register(Post)
admin.site.register(PRoduct)
admin.site.register(Profile)


