#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from ..forms import CallForm
from django.utils.html import escape
register = template.Library()

INVALID_TAGS = ['script',]

@register.simple_tag
def call_form_tag():
	callform = CallForm()
	return callform
