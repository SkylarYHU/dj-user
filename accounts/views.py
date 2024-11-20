from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustormUserChangeForm
from .models import CustomerUser

def register_view(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save() # 存储新用户
      login(request, user) # 注册后直接登录
      return redirect('profile')
  else:
    form = CustomUserCreationForm()
  return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
  return render(request, 'accounts/login.html')

def logout_view(request):
  if request.method == "POST":  # 确保只处理 POST 请求
      logout(request)
      return redirect('login')  # 登出后重定向到login

@login_required
def profile_view(request):
  user_form = CustormUserChangeForm(instance=request.user)
  password_form = PasswordChangeForm(user=request.user)

  if request.method == "POST":
    if 'update_profile' in request.POST:
      user_form = CustormUserChangeForm(request.POST, request.FILES, instance=request.user)
      if user_form.is_valid():
        user_form.save()
        return redirect('profile') # 更新成功后刷新页面
    elif 'change_password' in request.POST:
      password_form = PasswordChangeForm(user=request.user, data=request.POST)
      if password_form.is_valid():
        user = password_form.save()
        update_session_auth_hash(request, user)
        return redirect('profile')
     
  context = {
    'user_form': user_form,
    'password_form': password_form
  }
  return render(request, 'accounts/profile.html', context)

def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      # 更新会话，防止用户密码更改后被登出
      update_session_auth_hash(request, user)
      return redirect('profile')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'accounts/profile.html', {"form":form})


@login_required
def user_list_view(request):
  if request.user.is_superuser:
    users = CustomerUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users':users})
  return redirect('profile')