from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404


def post_list(request):
    context = {
        'post_list': Post.objects.filter(
            published_date__lte=timezone.now()
        ),
    }
    return render(request, 'blog/post-list.html', context)


def post_detail(request, post_id):
    # try:
    #     # ORM을 이용해서 id가 전달받은 post_id와 일치하는 Post객체를 post변수에 할당
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     return HttpResponse(e)

    post = get_object_or_404(Post, id=post_id)

    # 전달할 context 딕셔너리 키 'post'에 post 변수를 전달
    context = {
        'post': post,
    }
    # blog/post-detail.html 템플릿을 render한 결과를 리턴
    return render(request, 'blog/post-detail.html', context)
