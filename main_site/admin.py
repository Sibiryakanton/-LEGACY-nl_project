from django.contrib import admin
from .models import Sponsor, Category, CategoryElement, Post, Subcategory
from .models import OfferElement, Catalog, BusinessText, Video, SMTPMail, RecMail, BusinessBullet, Image

from .forms import ProductAdminForm, VideoAdminForm, SubcategoryForm

admin.site.register(Catalog)
admin.site.register(OfferElement)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Sponsor)
admin.site.register(BusinessText)
admin.site.register(SMTPMail)
admin.site.register(RecMail)
admin.site.register(BusinessBullet)
admin.site.register(Image)

class ProductAdmin(admin.ModelAdmin):
	form = ProductAdminForm
	
	list_display = ('published_date', 'title', 'category', 'subcategory', 'description','price','publish', 'prepared')
	list_display_links = ('title',)
	list_per_page=50
	ordering = ['-published_date','title', 'category', 'subcategory']
	search_field = ['title']
	exclude = ()
	
	
admin.site.register(CategoryElement, ProductAdmin)

class VideoAdmin(admin.ModelAdmin):
	form = VideoAdminForm
	
	list_display = ('title', 'video_url','in_gallery', 'priority')
	list_display_links = ('title',)
	list_per_page=50
	ordering = ['title']
	search_field = ['title']
	exclude = ()
	
admin.site.register(Video, VideoAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    form = SubcategoryForm
    
    list_display = ('title', 'slug',)
    list_display_links = ('title',)
    list_per_page = 50
    ordering = ['title']
    search_field = ['title']
    exclude=()
    prepopulated_fields={'slug':('title',)}
	
admin.site.register(Subcategory, SubcategoryAdmin)