'''
2020. 2.
'''
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse

from bs4 import BeautifulSoup

from rules.models import Rule, Filter, Attribute


def test(response):
    '''
    test function
    '''
    my_rule = Rule.objects.get(id=1)

    external_http = urllib.request.urlopen(my_rule.url)
    whole_html = external_http.read()
    data = BeautifulSoup(whole_html, 'html.parser')

    my_filters = Filter.objects.filter(origin_rule=my_rule)
    for ft in my_filters:
        my_attributes = Attribute.objects.filter(origin_filter=ft)
        att_dict = {}
        for att in my_attributes:
            att_dict[att.name] = att.value

        if ft.find_all:
            data = data.find_all(ft.tag_name, att_dict)
        else:
            data = data.find(ft.tag_name, att_dict)

    return HttpResponse(content=data)
