from ..utils import get_page_tree_information
from . import ModularPage


class MiniSiteNameSpace(ModularPage):
    subpage_types = [
        'CampaignPage',
        'OpportunityPage',
    ]

    """
    This is basically an abstract page type for setting up
    minisite namespaces such as "campaign", "opportunity", etc.
    """

    def get_context(self, request, *args, **kwargs):
        """
        Extend the context so that mini-site pages know what kind of tree
        they live in, and what some of their local aspects are:
        """
        context = super(MiniSiteNameSpace, self).get_context(request)
        updated = get_page_tree_information(self, context)
        updated['mini_site_title'] = updated['root'].title
        return updated

    class Meta:
        app_label = 'wagtailpages'
