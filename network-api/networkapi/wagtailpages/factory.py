from django.conf import settings
from factory.django import DjangoModelFactory
from wagtail_factories import (
    PageFactory,
    ImageFactory
)
from factory import (
    Faker,
    SubFactory,
    LazyAttribute,
    Trait,
)
from .models import (
    CampaignPage,
    Homepage,
    HomepageFeaturedNews,
    HomepageFeaturedHighlights,
    InitiativesPage,
    MiniSiteNameSpace,
    NewsPage,
    OpportunityPage,
    ParticipatePage,
    PeoplePage,
    Petition,
    PrimaryPage,
    Signup,
    Styleguide,
)
from .donation_modal import (
    DonationModal,
    DonationModals,
)
from networkapi.highlights.factory import HighlightFactory
from networkapi.news.factory import NewsFactory

sentence_faker: Faker = Faker('sentence', nb_words=3, variable_nb_words=False)
header_faker: Faker = Faker('sentence', nb_words=6, variable_nb_words=True)
description_faker: Faker = Faker('paragraphs', nb=6)


class CTAFactory(DjangoModelFactory):
    class Meta:
        abstract = True
        exclude = (
            'header_text',
            'description_text',
        )

    name = Faker('text', max_nb_chars=80)
    header = LazyAttribute(lambda o: o.header_text.rstrip('.'))
    description = LazyAttribute(lambda o: ''.join(o.description_text))
    newsletter = Faker('word')

    # Lazy Values
    description_text = description_faker
    header_text = header_faker


class PetitionFactory(CTAFactory):
    class Meta:
        model = Petition

    campaign_id = settings.PETITION_TEST_CAMPAIGN_ID


class DonationModalFactory(DjangoModelFactory):
    class Meta:
        model = DonationModal

    name = Faker('text', max_nb_chars=20)


class DonationModalsFactory(DjangoModelFactory):
    # note: plural!
    class Meta:
        model = DonationModals

    donation_modal = SubFactory(DonationModalFactory)


class SignupFactory(CTAFactory):
    class Meta:
        model = Signup


class WagtailHomepageFactory(PageFactory):
    class Meta:
        model = Homepage

    hero_headline = Faker('text', max_nb_chars=140)
    hero_story_description = Faker('paragraph', nb_sentences=5, variable_nb_sentences=True)
    hero_button_text = Faker('text', max_nb_chars=50)
    hero_button_url = Faker('url')
    hero_image = SubFactory(ImageFactory)


class CMSPageFactory(PageFactory):
    class Meta:
        abstract = True
        exclude = (
            'title_text',
            'header_text',
        )

    header = LazyAttribute(lambda o: o.header_text.rstrip('.'))
    title = LazyAttribute(lambda o: o.title_text.rstrip('.'))
    narrowed_page_content = Faker('boolean', chance_of_getting_true=50)

    # Lazy Values
    title_text = sentence_faker
    header_text = header_faker


class PrimaryPageFactory(CMSPageFactory):
    class Meta:
        model = PrimaryPage


class CampaignPageFactory(CMSPageFactory):
    class Meta:
        model = CampaignPage

    class Params:
        no_cta = Trait(cta=None)

    cta = SubFactory(PetitionFactory)


class MiniSiteNameSpaceFactory(PageFactory):
    class Meta:
        model = MiniSiteNameSpace


class PeoplePageFactory(PageFactory):
    class Meta:
        model = PeoplePage

    title = 'people'


class NewsPageFactory(PageFactory):
    class Meta:
        model = NewsPage

    title = 'news'


class StyleguideFactory(PageFactory):
    class Meta:
        model = Styleguide

    title = 'styleguide'


class InitiativesPageFactory(PageFactory):
    class Meta:
        model = InitiativesPage

    title = 'initiatives'


class ParticipatePageFactory(PageFactory):
    class Meta:
        model = ParticipatePage

    title = 'participate'


class OpportunityPageFactory(CMSPageFactory):
    class Meta:
        model = OpportunityPage

    class Params:
        no_cta = Trait(cta=None)

    cta = SubFactory(SignupFactory)


class FeaturedFactory(DjangoModelFactory):
    class Meta:
        abstract = True

    page = SubFactory(WagtailHomepageFactory)


class HomepageFeaturedNewsFactory(FeaturedFactory):
    class Meta:
        model = HomepageFeaturedNews

    news = SubFactory(NewsFactory)


class HomepageFeaturedHighlightsFactory(FeaturedFactory):
    class Meta:
        model = HomepageFeaturedHighlights

    highlight = SubFactory(HighlightFactory)
