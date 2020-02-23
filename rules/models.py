from django.db import models


class Rule(models.Model):
    url = models.CharField(max_length=1000)


class Filter(models.Model):
    tag_name = models.CharField(max_length=30)
    origin_rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    find_all = models.BooleanField()


class Attribute(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    origin_filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
