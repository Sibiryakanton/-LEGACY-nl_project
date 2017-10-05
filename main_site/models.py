#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from ckeditor.fields import RichTextField
from django.conf import settings


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    title = models.CharField("Заголовок", max_length=30)
    subcategory = models.ManyToManyField('Subcategory', verbose_name='Подкатегории', related_name='category', blank=True)
    photo = models.ImageField("Фото", upload_to="images/catalog", default="")
    slug = models.CharField("Метка(для URl-адреса)", max_length=30)
    on_index = models.BooleanField('Разместить на главной', default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, Category, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, Category, *args, **kwargs)


class Subcategory(models.Model):
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    title = models.CharField("Заголовок", max_length=30)
    slug = models.CharField("Метка (для URl-адреса)", max_length=30, default="")

    def __str__(self):
        return self.title


class CategoryElement(models.Model):

    class Meta:
        verbose_name = "Товарная карточка"
        verbose_name_plural = "Товарные карточки"

    title = models.CharField("Заголовок", max_length=30)
    photo = models.ImageField("Фото", upload_to="images/catalog_element", help_text='Основное фото для каталога. Остальные фото можно разместить в поле "Текст"')
    category = models.ForeignKey("Category", verbose_name="Категория")
    subcategory = models.ForeignKey('Subcategory', verbose_name='Подкатегории', default=0, blank=True)
    description = models.CharField("Краткое описание", max_length=100, help_text='1-2 предложения о продукте')
    full_text = RichTextField("Текст")
    price = models.IntegerField("Цена")
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)
    publish = models.BooleanField('Показывать в каталоге', default=True, blank=True)
    prepared = models.BooleanField('Полностью подготовлено', default=False, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, CategoryElement, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, CategoryElement, *args, **kwargs)


class OfferElement(models.Model):  # Представление для акций на главной
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    title = models.CharField("Заголовок", max_length=100)
    photo = models.ImageField("Фото", upload_to="images/offer")
    description = models.CharField("Краткое описание", max_length=300)
    text = RichTextField("Текст")
    published_date = models.DateTimeField("Дата публикации", blank=True, null=True)
    to_fix = models.BooleanField('Закрепить на главной', default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, OfferElement, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, OfferElement, *args, **kwargs)

class Sponsor(models.Model):  # Для раздела "Бизнес-проект"

    class Meta:
        verbose_name = "Лидер"
        verbose_name_plural = "Лидеры"
    surname = models.CharField("Фамилия", max_length=30)
    name = models.CharField("Имя", max_length=30)
    middle = models.CharField("Отчество", max_length=30)
    photo = models.ImageField("Фото", upload_to="images/sponsor", default='')
    refferal_url = models.CharField('Реферальная ссылка', max_length=200, default='')
    code_number = models.BigIntegerField("Код в NL", null=True, blank=True)
    on_business = models.BooleanField("Добавить в список на странице 'Бизнес-проект'", default=False)

    def __str__(self):
        code_number_2 = str(self.code_number)
        title = "{0} {1} {2} ({3})".format(self.name, self.surname, self.middle, code_number_2)
        return title

    def delete(self, *args, **kwargs):
        delete_model_object(self, Sponsor, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, Sponsor, *args, **kwargs)


class Video(models.Model):
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    title = models.CharField("Заголовок", max_length=100)
    video_url = models.URLField("URL-ссылка", max_length=200)
    priority = models.IntegerField('Приоритет в разделе "Видео"', default=1)
    in_gallery = models.BooleanField('Показывать в разделе "Видео"', default=False)

    def save(self, *args, **kwargs):
        self.video_url = self.video_url.replace("https://www.youtube.com/watch?v=", "https://www.youtube.com/embed/")
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
    title = models.CharField(max_length=150)
    photo = models.ImageField('Фото', upload_to='images/photos')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, Image, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, Image, *args, **kwargs)

class Post(models.Model):
    class Meta:
        verbose_name_plural = "Записи для Wellness"
        verbose_name = "Записи для Wellness"

    title = models.CharField("Заголовок", max_length=50)
    photo = models.ImageField("Фото", upload_to="welness_icons")
    description = models.CharField("Краткое описание", max_length=200)
    text = RichTextField(verbose_name="Текст")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, Post, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, Post, *args, **kwargs)


class Catalog(models.Model):
    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"

    title = models.CharField("Заголовок", max_length=100)
    # document = models.FileField(upload_to="catalog/", verbose_name="Файл")
    url = models.URLField(max_length=300, help_text='Ссылка на каталог в Google-документах')

    def save(self, *args, **kwargs):
        if "preview" not in self.url:
            self.url = self.url.replace("view", "preview")
        super(Catalog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BusinessText(models.Model):
    class Meta:
        verbose_name = "Бизнес-проект: текст для страницы"
        verbose_name_plural = "Бизнес-проект: текст для страниц"

    title = models.CharField("Заголовок", max_length=100)
    full_text = RichTextField("Текст")

    def __str__(self):
        return self.title


class RecMail(models.Model):
    class Meta:
        verbose_name = "Настройки уведомлений: ящики, принимающие заявки"
        verbose_name_plural = "Настройки уведомлений: ящики, принимающие заявки"

    name = models.CharField(max_length=100)
    mail = models.EmailField(verbose_name="Почтовый ящик")

    def __str__(self):
        return self.name + ", " + self.mail


class BusinessBullet(models.Model):
    class Meta:
        verbose_name = "бизнес-проект: буллет"
        verbose_name_plural = "бизнес-проект: буллеты"

    title = models.CharField("Заголовок", max_length=30)
    description = models.CharField("Описание", max_length=150)
    photo = models.ImageField("Фото", upload_to="images/business_bullet")
    text = models.TextField("Текст")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, BusinessBullet, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, BusinessBullet, *args, **kwargs)


class ReferralUrl(models.Model):
    class Meta:
        verbose_name = 'Реферальная ссылка'
        verbose_name_plural = 'Реферальные ссылки'

    title = models.CharField('Заголовок(для админки)', max_length=30)
    url = models.URLField('Ссылка',)
    photo = models.ImageField('Изображение', upload_to='images/referal_images')

    def __str__(self):
            return self.title

    def delete(self, *args, **kwargs):
        delete_model_object(self, ReferralUrl, *args, **kwargs)

    def save(self, *args, **kwargs):
        save_model_object(self, ReferralUrl, *args, **kwargs)


# Функции для удаления изображения вместе с объектом модели (с их введением объем половины моделей сократился минимум на треть)
def delete_model_object(obj, model, *args, **kwargs):
    super(model, obj).delete(*args, **kwargs)
    if obj.photo != '':
        storage, path = obj.photo.storage, obj.photo.path
        storage.delete(path)

def save_model_object(obj, model, *args, **kwargs):
    try:
        current_object = model.objects.get(pk=obj.pk)
        if current_object.photo != obj.photo:
            path = current_object.photo.path
            current_object.photo.storage.delete(path)
            current_object.photo = obj.photo
    except model.DoesNotExist:
        pass
    super(model, obj).save(*args, **kwargs)