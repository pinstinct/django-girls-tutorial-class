from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404

from .models import Post
from .forms import PostForm


def post_list(request):
    context = {
        # 'post_list': Post.objects.filter(
        #     published_date__lte=timezone.now()
        # ),
        'post_list': Post.objects.all()
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


def post_add(request):
    if request.method == 'POST':
        # 요청의 method가 POST일 경우
        # 요청받은 데이터를 출력
        data = request.POST
        # html의 name이 키값


        # PostForm에 data인자로 request.POST 데이터를 전달해준다
        form = PostForm(data=request.POST)
        # title = data['input_title']
        # content = data['input_content']
        author = User.objects.get(id=1)
        # print(request.POST)
        # ret = ','.join([title, content])

        # 만약 PostForm객체가 유효할 경우(전달된 데이터의 형식이 PostForm 에 정의한 형식과과 맞을 경우)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # 받은 데이터를 사용해세 Post 객체를 생성
            p = Post(title=title, content=content, author=author)
            p.save()

        else:
            return HttpResponse('Form invalid {}'.format(form.errors))

        # redirect메서드는 인자로 주어진
        # URL 또는
        # urlpattern의 name을 이용해 만들어낸 URL을 사용해서
        # 브라우저가 해당 URL로 이동하도록 해줌
        # 브라우저가 해당 URL로 이동하도록 해줌
        # return redirect('post_list')

        # 글 상세화면으로 이동 키워드(post_id)의 인자로 p.id를 전달
        return redirect('post_detail', post_id=p.id)


    else:
        # PostForm형 객체를 만들어 context에 할당
        form = PostForm()
        context = {
            'form': form,
        }
        # 요청의 method가 POST가 아닐 경우
        # 글 쓰기 양식이 있는 템플릿을 렌더해서 리턴
        return render(request, 'blog/post-add.html', context)
