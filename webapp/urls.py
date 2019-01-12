from django.urls import path
from webapp.views import MainView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, \
    UserListView, UserDetailView

app_name = 'webapp'

urlpatterns = [
    path('', MainView.as_view(), name = 'main_list'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('users/', UserListView.as_view(), name='users_list'),
    path('user/<int:pk>/detail', UserDetailView.as_view(), name='user_detail')
]

