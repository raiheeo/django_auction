from .models import Car, Brand, Model, 
from modeltranslation.translator import TranslationOptions,register


@register(Model)
class ModelTranslationOptions(TranslationOptions):
    fields = ('model_name', )

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('brand_name', )


