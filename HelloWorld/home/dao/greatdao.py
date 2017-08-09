# -*- coding: utf-8 -*-

from HelloWorld.home.models import Home


# 用户点赞
def add(ipadress):
    test1 = Home(ipadress=ipadress)
    test1.save()
    return 0

# 查询用户是否点赞过
def select(ipadress):
    response = Home.objects.filter(ipadress=ipadress)
    if(response):
        return True
    else:
        return False

# 查询点赞数
def selectnum():
    num = Home.objects.count()
    return num