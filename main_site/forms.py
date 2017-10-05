#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
import datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import *


def TakeAllObjects(x):
        return x.objects.all()


class Registration(forms.Form):
    email = forms.CharField(label='Почта', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'type': 'email', 'class': 'ftrmail'}))
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Пароль', 'class': 'ftrmail'}))
    lastname = forms.CharField(label='Фамилия', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'ftrmail'}))
    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'ftrmail'}))
    middlename = forms.CharField(label='Отчество', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'ftrmail'}))
    passport = forms.IntegerField(label='Номер и серия паспорта', validators=[RegexValidator('^(\(?\d{4}\)?[\- ]?)?(\(?\d{6}\)?[\- ]?)$')], widget=forms.TextInput(attrs={'placeholder': '0000 000000', 'pattern': "[0-9]{2} [0-9]{2} [0-9]{6}", 'class': 'ftrmail', 'title': 'Пример: 00 00 000000'}))
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'placeholder': 'День рождения (ДД/ММ/ГГГГ)', 'class': 'ftrmail', 'type': 'date'}))
    telephone = forms.CharField(label='Телефон', validators=[RegexValidator('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')], widget=forms.TextInput(attrs={'type': 'phone', 'id': 'user_phone_2', 'class': 'ftrmail', 'required': 'True', 'pattern': "[0-9_-]{10}", 'title': 'Пример: 8-888-888-88-88'}))
    region = forms.CharField(label='Область', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Область', 'class': 'ftrmail'}))
    index = forms.IntegerField(label='Индекс', widget=forms.TextInput(attrs={'placeholder': 'Почтовый индекс', 'class': 'ftrmail'}))
    district = forms.CharField(label='Район', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Район', 'class': 'ftrmail'}))
    town = forms.CharField(label='Город', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Город', 'class': 'ftrmail'}))
    street = forms.CharField(label='Улица', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Улица', 'class': 'ftrmail'}))
    number = forms.CharField(label='Номер дома и квартиры', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Номер дома и квартиры', 'class': 'ftrmail'}))
    sponsor = forms.ModelChoiceField(label='Спонсор', queryset=TakeAllObjects(Sponsor), empty_label='---', widget=forms.Select(attrs={'class': 'ftrmail'}))


class Call_Form(forms.Form):
    lastname = forms.CharField(label='Фамилия', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'ftrmail'}))
    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'ftrmail'}))
    middlename = forms.CharField(label='Отчество', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Отчество', 'class': 'ftrmail'}))
    birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'placeholder': 'День рождения (ДД/ММ/ГГГГ)', 'class': 'ftrmail', 'type': 'date'}))
    telephone = forms.CharField(label='Телефон', validators=[RegexValidator('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')], widget=forms.TextInput(attrs={'type': 'phone', 'id': 'user_phone', 'class': 'ftrmail', 'required': 'True', 'pattern': "[0-9_-]{10}", 'title': 'Пример: 8-888-888-88-88'}))


class Message_Form(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'ftrmail', 'placeholder': 'Имя'}))
    mail = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'ftrmail', 'type': 'email', 'placeholder': 'E-mail'}))
    msg = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'ftrtext', 'rows': '4', 'placeholder': 'Сообщение'}))


class Cards_Filter(forms.Form):
    name = forms.ModelChoiceField(label='Все категории', queryset=TakeAllObjects(Category), empty_label='---', widget=forms.Select(attrs={'class': "category_filter", 'name': 'subcategory'}))


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = CategoryElement
        fields = ('title', 'photo', 'category', 'subcategory', 'description', 'full_text', 'price', 'published_date', 'publish', 'prepared')

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Стоимость продукта должна быть больше нуля.')
        return self.cleaned_data['price']


class VideoAdminForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video_url', 'in_gallery', 'priority')


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ('title', 'slug')
