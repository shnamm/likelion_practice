from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'image', 'created_at', 'view_count', 'writer')
    # list_editable = ('content')
    list_filter = ('created_at',)
    search_fields = ('id',)
    search_help_text = '게시판 번호, 작성자검색이 가능합니다.'
    inlines = [CommentInline]  #게시글에 댓글 기능 추가

    actions = []
# admin.site.register(Comment)
