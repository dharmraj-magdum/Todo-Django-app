from django.shortcuts import render, redirect
from django.views import View
from ..form import TODOForm
from ..models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/home.html"

    def get_context_data(self, **kwargs):
        context = Todo.objects.filter(
            user=self.request.user.id).order_by('-priority')
        return {"todos": context, "title": "home"}


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'priority']
    template_name = "todo/todoForm.html"
    success_url = "/"
    # form_class = TODOForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form, *args, **kwargs)


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/'

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def test_func(self, *args, **kwargs):
        todo = self.get_object()
        if self.request.user == todo.user:
            return True
        return False


def change_status(request, id, status):
    todo = Todo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home-page')


# //===================================
#     def post(self, request):
#         user = None
#         form = None
#         if request.user.is_authenticated:
#             user = request.user
#             form = TODOForm(request.POST)
#             if form.is_valid():
#                 todo = form.save(commit=False)
#                 todo.user = user
#                 todo.save()
#                 return redirect("home-page")
#         else:
#             return render(request, 'todo/todoForm.html', context={'form': form})

#     def get(self, request):
#         form = TODOForm()
#         return render(request, 'todo/todoForm.html', context={'form': form})
