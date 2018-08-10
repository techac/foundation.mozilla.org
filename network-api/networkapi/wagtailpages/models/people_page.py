from . import PrimaryPage


class PeoplePage(PrimaryPage):
    parent_page_types = ['Homepage']
    template = 'wagtailpages/static/people_page.html'
