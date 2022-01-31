
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name = "Blog"),

    path('blogs/',  views.blogList, name = "blogList"),

    path('bloggers/', views.authorList, name = "authorList"),

    path('create/',  views.createBlog, name = "createBlog"),

    path('update/', views.updateBlog, name = "updateBlog"),

    path('update/<str:slug>/', views.updateBlogData, name = "updateBlogData"),
    
    path('delete/',  views.deleteBlog, name = "deleteBlog"),

    path('delete/<str:slug>/', views.deleteBlogData, name = "deleteBlogData"),

    path('search/', views.searchBlog, name = "searchBlog"),
    
    path('blogid/', views.getBlogId, name = "getBlogId"),

    path('blogger/',  views.getAuthorId, name = "getAuthorId"),

    path('<str:slug>/', views.getBlogById, name = "getBlogById"),

    path('blogger/<str:slug>/',  views.getAuthorById, name = "getAuthorById"),
    
    

    
]