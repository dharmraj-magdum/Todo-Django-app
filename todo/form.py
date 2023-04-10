from django.forms import ModelForm
from .models import Todo


class TODOForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'priority']

    def __init__(self, *args, **kwargs):
        super(TODOForm, self).__init__(*args, **kwargs)
        self.fields['priority'].empty_label = None
