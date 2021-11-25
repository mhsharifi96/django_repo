from django.contrib import admin
from .models import Post,Comment,Category,Tag,Question,Answer,SimplePost
# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SimplePost)