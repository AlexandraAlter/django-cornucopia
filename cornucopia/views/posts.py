from django.http import HttpResponse
from django.shortcuts import render

from . import boards


class PostsView(boards.BoardView):
    def get(self):
        return "Posts!"
