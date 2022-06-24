from django.urls import path
from . import views
from .Blog.blog import *

urlpatterns = [

    path('', views.home,name='home'),
    path('register', views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    # path('portfolio/<course_id>', views.courseDetail),

    path('post/<str:category_id>',views.list_posts,name='post'),
    path('post_details/<str:post_id>',views.postdetails,name='post_details'),
    path('contacts', views.Contact, name='contact'),
    path('AddBlog', (addPost.as_view()), name='AddBlog'),

    # API to post a comment
    path('postComment/<post_id>',views.postComment,name='postComment'),
    # path('stored', views.stored_procedure, name='stored_procedure'),
    path('storedpara', views.stored_procedure, name='stored_procedure')


]