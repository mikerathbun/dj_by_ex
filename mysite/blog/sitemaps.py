from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """
    Creates a sitemap for Post

    Here is some more info for this class
    """
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        """returns the time obj was updated """
        return obj.updated()
