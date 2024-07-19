from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView  # 追加
from .models import Blog, Category
from . forms import BlogForm
from django.urls import reverse_lazy

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


class BlogCreateView(CreateView):

    model = Blog
    form_class = BlogForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('blog:create_done')

    def get_context_data(self, **kwargs):

        context = super(BlogCreateView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['message_type'] = "create"
        return context


def create_done(request):
    # 登録処理が正常終了した場合に呼ばれる
    return render(request, 'blog/create_done.html')
