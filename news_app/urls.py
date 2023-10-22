from django.urls import path
from .views import news_list, news_detail, HomePageView, ContactPageView, errorPageView, aboutPageView, LocalNewsPage, \
                WorldNewsPage, TechnologyNewsPage, SportNewsPage

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name="all_news_list"),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name="contact_page"),
    path('error-404/', errorPageView, name="error_page"),
    path('about/', aboutPageView, name="about_page"),
    path('local/', LocalNewsPage.as_view(), name='local_news_page'),
    path('world/', WorldNewsPage.as_view(), name='world_news_page'),
    path('technology/', TechnologyNewsPage.as_view(), name='technology_news_page'),
    path('local/', SportNewsPage.as_view(), name='sport_news_page'),
]