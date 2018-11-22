from django.shortcuts import render,redirect,HttpResponse
from . import models
from . import forms

# Create your views here.


def index(request):
    return render(request,"user/index.html")

def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return redirect("/index/")
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
            return render(request,"user/login.html",locals())
    login_form = forms.UserForm()
    return render(request,"user/login.html",locals())

def logout(request):
    return redirect("/login/")
