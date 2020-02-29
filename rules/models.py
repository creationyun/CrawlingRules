''' Django DB Models '''
from django.db import models


class Rule(models.Model):
    ''' URL Crawling Rule Declaration '''
    url = models.CharField(max_length=1000)


class Filter(models.Model):
    ''' Tag Filters of Crawling Rule '''
    tag_name = models.CharField(max_length=30)
    origin_rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    find_all = models.BooleanField()


class Attribute(models.Model):
    ''' Attributes of Tag in Filters  '''
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    origin_filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
