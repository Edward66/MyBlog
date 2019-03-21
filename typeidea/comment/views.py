from django.views.generic import TemplateView
from django.shortcuts import redirect

from .forms import CommentForm


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')

        if comment_form.is_valid():
            instance = comment_form.save(commit=False)  # If not committing, add a method to the form to allow deferred
            instance.target = target  # 保存当前路径到数据库（form表单中没有写这个字段)
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context)
