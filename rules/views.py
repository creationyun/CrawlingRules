''' views.py: Page view methods and some tool functions '''
import urllib.request
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.urls import reverse

from bs4 import BeautifulSoup

from rules.models import Rule, Filter, Attribute
from rules.forms import FilterForm, AttributeForm


def main(request):
    ''' main page rendering function '''

    url_save_successful = 0  # this value is rule's id
    rule_page = 1  # this value is first shown rule page

    if request.method == 'GET' and 'rule_page' in request.GET:
        # Load GET parameters (/?rule_page=??)
        rule_page = int(request.GET['rule_page'])

    if request.method == 'POST':
        if request.POST['rules_submit'] == 'set_url':
            # URL related POST Request
            rule_id = int(request.POST['rule_id'])
            rule = get_object_or_404(Rule, id=rule_id)
            rule.url = request.POST['rule_url']
            rule.save()
            url_save_successful = rule_id
            rule_page = rule_id

        if request.POST['rules_submit'] == 'add_rule':
            # Add new rule related POST Request
            new_rule = Rule.objects.create()
            return HttpResponseRedirect(reverse('main') + '?rule_page=%s' % new_rule.id)

        if request.POST['rules_submit'] == 'add_filter':
            # Add new filter related POST Request
            rule_id = int(request.POST['rule_id'])
            Filter.objects.create(
                origin_rule=Rule.objects.get(id=rule_id),
                tag_name=request.POST['addFilterTagName'],
                find_all=False
            )
            return HttpResponseRedirect(reverse('main') + '?rule_page=%s' % rule_id)

        if request.POST['rules_submit'] == 'remove_rule':
            # Remove the rule related POST Request
            rule_id = int(request.POST['rule_id'])
            rule = get_object_or_404(Rule, id=rule_id)
            filts_in_rule = Filter.objects.filter(origin_rule=rule)
            for filt in filts_in_rule:
                attrs_in_filter = Attribute.objects.filter(origin_filter=filt)
                for att in attrs_in_filter:
                    att.delete()
                filt.delete()
            rule.delete()
            return redirect('main')

    context = {
        'rules': Rule.objects.all(),
        'url_save_successful': url_save_successful,
        'rule_page': rule_page
    }

    return render(request, 'sites/rules.html', context)


@xframe_options_exempt
def test_view(request, rule_id):
    ''' test view function '''
    return HttpResponse(content=crawling(rule_id))


def filter_settings(request, filter_id):
    ''' filter settings page rendering function '''

    filt = get_object_or_404(Filter, id=filter_id)
    filtform = FilterForm(request.POST or None, instance=filt)

    if request.method == 'POST':
        if request.POST['filter_submit'] == 'save_filter' and filtform.is_valid():
            # Save filter settings related POST request
            filtform.save()
            return redirect('main')

        if request.POST['filter_submit'] == 'add_attribute':
            # Create new filter's attribute related POST request
            name = request.POST['createAttrName']
            value = request.POST['createAttrValue']
            origin_filt = Filter.objects.get(id=filter_id)
            Attribute.objects.create(
                name=name, value=value, origin_filter=origin_filt)
            return redirect('filter_settings', filter_id=filter_id)

        if request.POST['filter_submit'] == 'delete_filter':
            # Delete filter related POST request
            attrs_in_filter = Attribute.objects.filter(origin_filter=filt)
            for att in attrs_in_filter:
                att.delete()
            filt.delete()
            return redirect('main')

    context = {
        'filter': filt,
        'form': filtform
    }

    return render(request, 'sites/filter_settings.html', context)


def attr_settings(request, attr_id):
    ''' attribute settings page rendering function '''

    attr = get_object_or_404(Attribute, id=attr_id)
    attrform = AttributeForm(request.POST or None, instance=attr)

    if request.method == 'POST':
        if request.POST['attr_submit'] == 'save_attribute' and attrform.is_valid():
            # Save attribute settings related POST request
            attrform.save()
            return redirect('main')

        if request.POST['attr_submit'] == 'delete_attribute':
            # Delete attribute related POST request
            attr.delete()
            return redirect('main')

    context = {
        'attribute': attr,
        'form': attrform
    }

    return render(request, 'sites/attr_settings.html', context)


def crawling(id_idx):
    ''' Crawling method with django models '''
    # get first rule
    my_rule = Rule.objects.get(id=id_idx)

    # init bs4 -> data (soup)
    external_http = urllib.request.urlopen(my_rule.url)
    whole_html = external_http.read()
    data = BeautifulSoup(whole_html, 'html.parser')

    # finding process with filters
    my_filters = Filter.objects.filter(origin_rule=my_rule)
    for filt in my_filters:
        my_attributes = Attribute.objects.filter(origin_filter=filt)
        att_dict = {}
        for att in my_attributes:
            att_dict[att.name] = att.value

        if filt.find_all:
            data = data.find_all(filt.tag_name, att_dict)
        else:
            data = data.find(filt.tag_name, att_dict)

    return str(data)
