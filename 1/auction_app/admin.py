from django.contrib import admin
from .models import Auction, Feedback, Bid, UserProfile, Car, Brand, Model
from modeltranslation.admin import TranslationAdmin


@admin.register(Car, Brand, Model)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Bid)
admin.site.register(Feedback)
admin.site.register(Auction)




