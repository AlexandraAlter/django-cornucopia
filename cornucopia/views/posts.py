from django import http, views

from . import boards


class PostListView(views.View):
    pass


class DeletedPostListView(views.View):
    pass


class NewPostView(views.View):
    pass


class PostView(views.View):
    pass


class EditPostView(views.View):
    pass


class PostHistoryView(views.View):
    pass


class ApprovePostView(views.View):
    pass


class DisapprovePostView(views.View):
    pass


class ReportPostView(views.View):
    pass


class AppealPostView(views.View):
    pass
