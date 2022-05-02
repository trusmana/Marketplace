from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.accounts.models import AccountsUser as user

@login_required
def home_member(request):
    user = request.user
    return render(request,'member/home-member.html',{'user':user})


def error_404(request,exception=None):
    context = {}
    return render(request,'core/error_500.html',context)

def error_500(request):
    context = {}
    return render(request,'core/error_500.html', context)
