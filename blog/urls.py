
from django.urls import path
from .views import PostDetail, PostList, add_comment

urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('<slug:slug>', PostDetail.as_view(), name='single'),
    # path('post/<slug:slug>', PostDetail.as_view(), name='single'),
    path('addcomment/', add_comment, name='addcomment'),
]
