from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def index(request):  # 関数ベース
    # TOP画面を表示する関数
    # return render(request, 'index.html')
    print("index関数を使ってTOP画面を表示します！関数ベース")
    return render(request, 'blog/index.html')  # 変更箇所


class IndexView(TemplateView):  # クラスベース
    # TOP画面を表示するクラス
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print("IndexViewを使ってTOP画面を表示します！クラスベース")
        return self.render_to_response(context)