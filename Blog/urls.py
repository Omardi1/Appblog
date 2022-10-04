from django.urls import path
from .views import  edit_article, home, about, article_list, article_details, new_article, edit_article
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', home, name="index"),
   path("about", about, name="about"),
   path("Article", article_list, name="Article"),
   path("Article/new", new_article, name="Article/new"),
   path("Article/<int:id>/", article_details, name="details"),
   path("Article/edit/<int:id>/", edit_article, name="edit_article"),
#]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

   ]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)       


