from django.shortcuts import render, redirect
from django.views import View
from ..models import Todo


class HomeView(View):

    def get(self, request):
        todos = []
        if request.user.is_authenticated:
            todos = Todo.objects.filter(
                user=request.user.id).order_by('-priority')
        return render(request, "todo/home.html", {"todos": todos})
