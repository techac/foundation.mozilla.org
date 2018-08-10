from . import PrimaryPage


class NewsPage(PrimaryPage):
    parent_page_types = ['Homepage']
    template = 'wagtailpages/static/news_page.html'
