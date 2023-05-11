from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Post
from .forms import PostBaseForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    post_list = Post.objects.all() #Post 전체 데이터 조회
    post_list = Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인인 것 조회
    context = {
        'post_list' : post_list,
    }
    return render(request, 'posts/post_detail.html', context)
    return render(request, 'posts/post_list.html')

def post_detail_view(request):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context = {
        'post' : post
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        Post.objects.create(
            image = image,
            content = content,
            writer = request.user
        )
        return redirect('index')

def post_create_form_view(request):
    if request.method == 'GET':
        form = PostBaseForm()
        return render(request, 'posts/post_form.html', {'form':form})
    else:
        form = PostBaseForm(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user
            )
        else:
            return redirect('post:post-create')
        return redirect('index')

@login_required
def post_update_view(request):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        context = {'post' : post}
        return render(request, 'posts.post_form.html', context)
    elif request.method == 'POST':
        new_image = request.FILES.get('image')
        content = request.POST.get('content')
        if new_image:
            post.image.delete()  #기존 이미지 삭제 후 추가
            post.image = new_image
        post.content = content
        post.save()
        return redirect('post:post-detail', post.id)
@login_required
def post_delete_view(request):
    post = get_object_or_404(Post, id=id)
    if request.user != post.writer:
        return Http404('잘못된 접근입니다.')
    if request.method == 'GET':
        context = {'post' : post}
        return render(request, 'posts/post_confirm_delete.html', context)
    else:
        post.delete()
        return redirect('index')

def url_view(request):
    data = {'code': '001', 'msg': 'ok'}
    return HttpResponse('<h1>url_view</h1>')
    # return JsonResponse(data)

def url_parameter_view(request, username):
    print(username)
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
        print(f'request.GET: {request.GET}')
    else:
        print(f'request.POST: {request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model = Post
    template_name = 'cbv_views.html'