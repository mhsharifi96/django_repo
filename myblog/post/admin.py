from django.contrib import admin
from .models import Post,Comment,Category,Tag,Question,Answer,SimplePost
from django.utils.html import format_html


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(SimplePost)


class CommentInline(admin.TabularInline):
    model = Comment


    


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','shortdesc','created_on','owner','status','view_title_desc','show_image')
    list_filter = ('status','created_on','category')
    search_fields = ('title','shortdesc')
    date_hierarchy = ('created_on')

    @admin.display(empty_value='-',description="title desc")
    def view_title_desc(self, obj):
        if (obj.image):
            print(obj.image.url)
        print(type(obj))
        return format_html(
             '<span style="color: red;">{} {}</span>',
            obj.title,
            obj.desc,
        )
        # return obj.shortdesc obj.title
        # return f'{} {}'
    @admin.display(empty_value='-',description="show image")
    def show_image(self, obj):
        if (obj.image):
            print(obj.image.url)
        
            return format_html(
                '<img src="{}" width=50 height=50/>',
                obj.image.url,
                
            )
        return '-'
    
    # fields = (('title','shortdesc'),'desc',('owner','status'))
    fieldsets = (
        (None, {
            'fields': (('title', 'shortdesc'), 'desc', 'owner')
        }),

        ('maktab sharif', {
            'classes': ('collapse',),
            'fields': ('location_lng','location_lat'),
        }),
    )
    # save_on_top =True
    inlines = [
        CommentInline,
    ]
    # list_per_page = 10
    list_editable = ('shortdesc','status')
admin.site.register(Post,PostAdmin)