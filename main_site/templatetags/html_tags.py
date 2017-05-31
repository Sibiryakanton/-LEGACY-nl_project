#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
from ..forms import Call_Form
from django.utils.html import escape
register = template.Library()
INVALID_TAGS = ['script',]


@register.simple_tag
def CallForm_tag():
	callform = Call_Form()
	return callform
