from django import http, views

from ..models.boards import Board


class BoardMixin:
    def get_board(self):
        # get_object_or_404 here?
        board_name = self.kwargs.get('board_name')
        board = Board.objects.filter(name=board_name).first()
        return board


class BoardListView(views.View):
    pass


class NewBoardView(views.View):
    pass


class BoardView(BoardMixin, views.View):
    def get(self, request, *args, **kwargs):
        board = self.get_board()
        return http.HttpResponse("It's board number {}".format(board.id))
