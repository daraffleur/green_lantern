from apps.articles.views import SearchResultsView, main_page_logged_in, ShowTitsViews, \
    ArticleDetailView, ArticleUpdateImageView, ArticleListView, delete_view, ArticleCreate, ArticleView
from django.urls import path

from .views import update_view, detail_view

app_name = 'articles'

urlpatterns = [
    path('search/<int:some_id>', main_page_logged_in, name='main-page2'),
    path('search/', main_page_logged_in, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('tits_list/', ShowTitsViews.as_view(), name='tits'),
    path('<int:id>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:id>/change_image', ArticleUpdateImageView.as_view(), name='update_image'),
    path('article_list/', ArticleListView.as_view(), name='article-lists'),
    path('<id>/delete_article/', ArticleDetailView.as_view()),
    path('<id>/delete', delete_view),
    path('<id>/', detail_view),
    path('<id>/update', update_view),
    path('', ArticleCreate.as_view()),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view())

]
