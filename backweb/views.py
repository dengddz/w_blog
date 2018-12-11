from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect
from backweb.models import MyUser, Article
from backweb.Artform import AddArtForm, EditArtForm


def index(request):
    if request.method == 'GET':
        return render(request, 'backweb/index.html')
    
    
def register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = MyUser.objects.filter(username=username).first()
        if user:
            err_name = '该账号已被注册'
            return render(request, 'backweb/register.html', {'err_name':err_name})
        
        if password and password2:
            if password != password2:
                err_pwd = '密码和确认密码不一致'  
                return render(request, 'backweb/register.html', {'err_pwd':err_pwd})
       
            user = MyUser()
            user.username = username
            user.password = password
            user.save()
        return render(request, 'backweb/login.html')
    
        
def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = MyUser.objects.filter(username=username, password=password).first()
        if not user:
            err = '用户名或密码错误'
            return render(request, 'backweb/login.html', {'err':err})
        request.session['user_id'] = user.id
        res = HttpResponseRedirect('/backweb/index/')
        return res
 
   
def article(request):
    if request.method == 'GET':   
        page = int(request.GET.get('page',1))
        articles = Article.objects.all()
        paginator = Paginator(articles,2)
        page = paginator.page(page)
        return render(request, 'backweb/article.html', {'page':page})
    
    
def add_article(request):
    if request.method == 'GET':
        return render(request, 'backweb/add-article.html')
    
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title, content=content, icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            return render(request, 'backweb/add-article.html ',{'form':form})
        
        
def edit_article(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add-article.html', {'article':article})
    if request.method == 'POST':
        form = EditArtForm(request.POST.request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['contnet']
            icon = form.cleaned_data['icon']
            article = Article.objects.filter(pk=id).first()
            article.title = title
            article.content = content
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add-article.html', {'form':form, 'article':article})
  
        
def del_article(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:article'))
        

