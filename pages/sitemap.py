from flask import (
    Blueprint,
    render_template
)
# from scrapy.contrib.spiders import SitemapSpider




bp = Blueprint(
    "sitemap", __name__,
    template_folder='templates',
    static_folder='static'
)
# class TestSpider(SitemapSpider):
#     name = 'test'
#     sitemap_urls = ['../static/sitemap.xml']
#     def parse(self, response):
#         pass

@bp.route("/site-map")
def index():
    # return render_template(".html")
    return "works"
    # return  TestSpider.parse()