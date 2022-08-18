from unicodedata import name
from django.urls import path
from . import views
from .views import AddCategoryview, AddCommentview, AddPostview, HomeView, articleview,UpdatePostView,DeletePostView,AddContactview #CategoryView
    
urlpatterns = [

    path('homeview/', HomeView.as_view(), name="homeview"),
    path('article/<int:pk>', articleview.as_view(), name="article_detail"),
    path('add_category/', AddCategoryview.as_view(), name="Category"),
    path('add_post/', AddPostview.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update_view"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete_view"),
    # path('category/<str:cats>/',CategoryView,name="category_view"),
    path('article/<int:pk>/comment/', AddCommentview.as_view(), name='add_comment'),
    # path('contact/', views.AddContactview, name='contact'),
     path('contact/', AddContactview.as_view(), name="contact"),
    
]