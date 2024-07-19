from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView  # 追加
from .models import Blog, Category
from . forms import BlogForm
from django.urls import reverse_lazy
from django.db.models import Q

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
        return context


def create_done(request):
    # 登録処理が正常終了した場合に呼ばれるテンプレートを指定
    category_list = Category.objects.all()  # 追加
    return render(request, 'blog/create_done.html', {
        'category_list': category_list})  # category_listを追加


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class BlogDeleteView(DeleteView):

    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:delete_done')

    def get_context_data(self, **kwargs):
        context = super(BlogDeleteView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


def delete_done(request):
    category_list = Category.objects.all()
    return render(request, 'blog/delete_done.html', {
        'category_list': category_list})


class CategoryView(ListView):
    """カテゴリ名でフィルタ検索"""
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        """カテゴリでの絞り込み"""
        category_name = self.kwargs['category']
        queryset = Blog.objects.filter(category__category_name=category_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class SearchPostView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        """
        request.GETには GET リクエストのパラメータが含まれています。
        request.GET.get('q', None)でqパラメータの値を取得し、値が
        存在しない場合はNoneを取得します。
        """
        query = self.request.GET.get('q', None)

        if query is not None:
            qs = Blog.objects.filter(Q(title__icontains=query) |
                                     Q(category__category_name__icontains=query))
            return qs

        else:
            qs = Blog.objects.all()
            return qs

    def get_context_data(self, *args, **kwargs):
        """クリックされたカテゴリを保持"""
        # context = super().get_context_data(*args, **kwargs)
        context = super(SearchPostView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
