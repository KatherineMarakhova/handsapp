from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='newshomepage'),
    path('addnew', views.add_new, name='addnews'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name="article-detail"),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name="article-update"),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name="article-delete"),
]
