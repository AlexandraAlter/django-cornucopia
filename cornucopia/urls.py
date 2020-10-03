from django.urls import include, path

from .views import (auth as v_auth, boards as v_boards, galleries as v_galleries, management as
                    v_management, posts as v_posts, root as v_root, tags as v_tags, tokens as
                    v_tokens, users as v_users)


def _reportable():
    return [
        path('report/new'),
        path('report/<int:report_id>'),
        path('reports/'),
    ]


_token = [
    path('tokens/', v_tokens.TokenListView.as_view()),
    path('tokens/new', v_tokens.NewTokenView.as_view()),
    path('token/<int:token_id>', v_tokens.TokenView.as_view()),
]

# Views into posts through other classes, like users, or the root.
# You can't create a new post from here, or view individual posts.
_post_virtual = [
    path('posts/', v_posts.PostListView.as_view()),
    path('posts/deleted', v_posts.DeletedPostListView.as_view()),
]

# Views that manipulate posts.
# Includes all virtual views.
_post_real = [
    path('posts/new', v_posts.NewPostView.as_view()),
    path(
        'post/<int:post_id>/',
        include([
            path('', v_posts.PostView.as_view()),
            path('edit/', v_posts.EditPostView.as_view()),
            path('history/', v_posts.PostHistoryView.as_view()),
            path('approve/', v_posts.ApprovePostView.as_view()),
            path('disapprove/', v_posts.DisapprovePostView.as_view()),
            path('report/', v_posts.ReportPostView.as_view()),
            path('appeal/', v_posts.AppealPostView.as_view()),
        ] + _token))
] + _post_virtual

_board = [
    path('boards/', v_boards.BoardListView.as_view()),
    path('boards/new', v_boards.NewBoardView.as_view()),
    path(
        'board/<slug:board_name>/',
        include([
            path('', v_boards.BoardView.as_view()),
            path('tag/<str:tag_name>', v_tags.TagView.as_view()),
            path('tags/', v_tags.TagListView.as_view()),
            path('tags/aliases', v_tags.TagAliasView.as_view()),
            path('tags/implications', v_tags.TagImplicationView.as_view()),
            path('galleries/', v_galleries.GalleryListView.as_view()),
            path('galleries/new', v_galleries.NewGalleryView.as_view()),
            path('gallery/<int:gallery_id>/',
                 include([
                     path('', v_galleries.GalleryView.as_view()),
                 ] + _token)),
        ] + _post_real + _token)),
]

urlpatterns = [
    path('', v_root.RootView.as_view()),
    path('home/', v_users.HomeView.as_view()),
    path('login/', v_auth.LoginView.as_view()),
    path('login/request/', v_auth.LoginRequestView.as_view()),
    path('login/invite/', v_auth.LoginInviteView.as_view()),
    path('logout/', v_auth.LogoutView.as_view()),
    path(
        'management/',
        include([
            path('', v_management.ManagementView.as_view()),
            path('reports/', v_management.ReportListView.as_view()),
            path('appeals/', v_management.AppealListView.as_view()),
        ])),
    path('users/', v_users.UserListView.as_view()),
    path(
        'user/<slug:username>/',
        include([
            path('', v_users.UserView.as_view()),
            path('report/', v_users.ReportUserView.as_view()),
        ] + _board + _post_virtual)),
] + _board + _post_virtual
