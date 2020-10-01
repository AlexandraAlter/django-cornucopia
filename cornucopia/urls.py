from django.urls import include, path

from . import views

_token = [
    path('tokens/', views.in_development),
    path('tokens/new', views.in_development),
    path('token/<int:token_id>', views.in_development),
]

# Views into posts through other classes, like users, or the root.
# You can't create a new post from here, or view individual posts.
_post_virtual = [
    path('posts/', views.in_development),
    path('posts/deleted', views.in_development),
]

# Views that manipulate posts.
# Includes all virtual views.
_post_real = [
    path('posts/new', views.in_development),
    path(
        'post/<int:post_id>/',
        include([
            path('', views.posts.PostsView.as_view()),
            path('edit/', views.in_development),
            path('history/', views.in_development),
            path('approve/', views.in_development),
            path('disapprove/', views.in_development),
            path('report/', views.in_development),
            path('appeal/', views.in_development),
        ] + _token))
] + _post_virtual

_board = [
    path('boards/', views.in_development),
    path('boards/new', views.in_development),
    path(
        'board/<slug:board_name>/',
        include([
            path('', views.boards.BoardView.as_view()),
            path('tag/<str:tag_name>', views.in_development),
            path('tags/', views.in_development),
            path('tags/aliases', views.in_development),
            path('tags/implications', views.in_development),
            path('galleries/', views.in_development),
            path('galleries/new', views.in_development),
            path('gallery/<int:gallery_id>/', include([
                path('', views.in_development),
            ] + _token)),
        ] + _post_real + _token)),
]

urlpatterns = [
    path('', views.in_development),
    path('home/', views.in_development),
    path('login/', views.in_development),
    path('login/request/', views.in_development),
    path('login/invite/', views.in_development),
    path('logout/', views.in_development),
    path('users/', views.in_development),
    path(
        'management/',
        include([
            path('', views.in_development),
            path('reports/', views.in_development),
            path('appeals/', views.in_development),
        ])),
    path('user/<slug:username>/',
         include([
             path('', views.in_development),
             path('report/', views.in_development),
         ] + _board + _post_virtual)),
] + _board + _post_virtual
