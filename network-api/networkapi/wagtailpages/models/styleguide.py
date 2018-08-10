from . import PrimaryPage


class Styleguide(PrimaryPage):
    parent_page_types = ['Homepage']
    template = 'wagtailpages/static/styleguide.html'
