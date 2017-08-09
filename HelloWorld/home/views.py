# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import json
from dao.greatdao import add, select, selectnum
from libs.utils.ip import getIP
# Create your views here.

def hello(request):
    ip = getIP(request)
    boolean = select(ip)
    print ip
    num = selectnum()
    obj = {"num": num,"boolean": boolean}
    temp = (request.GET['cb']+"(%s)") % (json.dumps(obj))
    return HttpResponse(temp)


def clickgood(request):
    ip = getIP(request)
    print ip
    boolean = select(ip)
    if (boolean):
        temp = (request.GET['cb'] + "(%s)") % "1"
        return HttpResponse(temp)
    else:
        obj = {"success": add(ip)}
        temp = (request.GET['cb'] + "(%s)") % (json.dumps(obj))
        return HttpResponse(temp)