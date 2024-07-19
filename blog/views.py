from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView  # 追加
from .models import Blog, Category

# Create your views here.


def index(request):  # 関数ベース
    # TOP画面を表示する関数
    # return render(request, 'index.html')
    print("index関数を使ってTOP画面を表示します！関数ベース")
    return render(request, 'blog/index.html')


class IndexView(TemplateView):  # クラスベース
    # TOP画面を表示するクラス
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("IndexViewを使ってTOP画面を表示します！クラスベース")
        return self.render_to_response(context)


class BlogListView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
