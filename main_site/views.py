#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse

from .models import Catalog, Category, CategoryElement, OfferElement, Post, BusinessText, Sponsor, Video, RecMail, BusinessBullet, Subcategory
from .forms import CallForm, Registration, MessageForm, CardsFilter
import sys

from django.core.mail import send_mail, get_connection

class Empty(object):
    def __init__(self, title):
        self.title = title

# Представление для главной страницы
def main(request):
    category = Category.objects.filter(on_index=True).order_by('id')[:4]
    list_fix = OfferElement.objects.filter(to_fix=True).order_by('-id')[:3]

    def fill_number():
        return 3 - len(list_fix)  # Если просто попытаться запросить в переменной 
                                  # длину списка, когда база еще пуста, выдает ошибку
    number = fill_number()
    list_offer = OfferElement.objects.filter(to_fix=False).order_by('-id')[: number]
    return render(request, 'index.html', {'list': list_offer, 'list_fix': list_fix, 'category': category})


def catalog(request):  # Представление для страницы PDF-каталога
    catalog_list = Catalog.objects.all().order_by('-id')
    catalog = Empty('На сайте нет ни одного каталога')

    if len(catalog_list) != 0:
        catalog = catalog_list[0]

    return render(request, 'catalog.html', {'catalog': catalog})


def category(request, slug):  # Представление товаров
    if request.method == 'POST':
        sub_title = request.POST.get('name', '')
        category_slug = request.POST.get('cur_category', '')
        current_subcategory = Subcategory.objects.get(pk=sub_title)
        category = Category.objects.get(slug=category_slug)
        all_subcategory = category.subcategory.all()
        cards = CategoryElement.objects.filter(subcategory=current_subcategory, category=category).order_by('-published_date')
    else:
        category = Category.objects.get(slug=slug)
        all_subcategory = category.subcategory.all()
        cards = CategoryElement.objects.filter(category=category).order_by('-published_date')
    paginator = Paginator(cards, 15)
    page = request.GET.get('page')
    card_filter = CardsFilter()
    
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)
    return render(request, 'forsome.html', {'cards': cards, 'category': category, 'page': page, 'filter': card_filter, 'subcat': all_subcategory})


def category_description(request, pk):  # Описание отдельного товара
    current_card = CategoryElement.objects.get(pk=pk)
    return render(request, 'description.html', {'current_card': current_card})


def wellness(request):
    wellness_list = Post.objects.all().order_by('-id')
    return render(request, 'wellness.html', {'wellness': wellness_list})


def stock_detail(request, pk):  # Детали акции на главной
    current_article = OfferElement.objects.get(pk=pk)
    return render(request, 'article.html', {'article': current_article})


def post_detail(request, pk):
    current_article = Post.objects.get(pk=pk)
    return render(request, 'article.html', {'article': current_article})


def bullet_detail(request, pk):  # Пункты списка в Бизнес-проекте
    current_article = BusinessBullet.objects.get(pk=pk)
    return render(request, 'article.html', {'article': current_article})


def business(request):  # Представление страницы Бизнес-проект
    text_business = BusinessText.objects.all()
    bullets = BusinessBullet.objects.all()
    sponsors = Sponsor.objects.filter(on_business=True)
    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            return redirect('/thanks/')
        else:
            return redirect('/error/')
    else:
        form = MessageForm()
    return render(request, 'business.html', {'text': text_business, 'sponsors': sponsors, 'bullets': bullets, 'form': form})


def video_gallery(request):
    video_list = Video.objects.filter(in_gallery=True).order_by('-priority')
    paginator = Paginator(video_list, 10)
    page = request.GET.get('page')
    try:
        video_list = paginator.page(page)
    except PageNotAnInteger:
        video_list = paginator.page(1)
    except EmptyPage:
        video_list = paginator.page(paginator.num_pages)
    return render(request, 'videogallery.html', {'video_list': video_list, 'page': page})


def form_call(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        name = request.POST.get('name', '')
        lastname = request.POST.get('lastname', '')
        middlename = request.POST.get('middlename', '')
        birthday = request.POST.get('birthday', '')
        telephone = request.POST.get('telephone', '')
        if form.is_valid():
            mail_host = 'orilamesender@gmail.com'
            rec_list = RecMail.objects.all()
            recipients = []
            for mail in rec_list:
                recipients.append(mail.mail)  # Список получателей
            message = '''
                На сайте вашей структуры NL International появилась новая заявка на звонок! Вот данные, предоставленные новым консультантом:
                ФИО:{0} {1} {2}
                Дата рождения: {3}
                Телефон: {4}'''.format(name, lastname, middlename, birthday, telephone)
            subject = 'Заявка на звонок'
            send_mail(subject, message, mail_host, recipients, fail_silently=False)
            return redirect('/thanks/')
        else:
            return redirect('/error/')


def message_call(request):
    if request.POST:
        form = MessageForm(request.POST)
        name = request.POST.get('name', '')
        mail = request.POST.get('mail', '')
        msg = request.POST.get('msg', '')
        if form.is_valid():
            mail_host = 'orilamesender@gmail.com'
            rec_list = RecMail.objects.all()
            recipients = []
            for mail in rec_list:
                recipients.append(mail.mail)  # Список получателей
            message = '''
                На сайте вашей структуры NL International пришло сообщение от пользователя {0} с ящика {1}! Вот его содержание:
                ___
                Сообщение: {2}'''.format(name, mail, msg)
            subject = 'Сообщение на сайте'
            send_mail(subject, message, mail_host, recipients, fail_silently=False)
            return redirect('/thanks/')
        else:
            return redirect('/error/')


def thanks(request):
    return render(request, 'thanks.html', {})
