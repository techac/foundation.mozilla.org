from . import PrimaryPage


class ParticipatePage(PrimaryPage):
    parent_page_types = ['Homepage']
    template = 'wagtailpages/static/participate_page.html'
