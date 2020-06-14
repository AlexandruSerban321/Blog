from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from posts.models import Post


class StaticViewsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['home', 'about', 'contact', 'browse', 'search']

    def location(self, item):
        return reverse(item)


class PostsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()
