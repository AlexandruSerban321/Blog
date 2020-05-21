from django.contrib import admin
from .models import Post, Category, Author, PostImage

admin.site.register(Category)
admin.site.register(Author)


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Post


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
