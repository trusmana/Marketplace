from django.contrib import admin
from . models import Jenis_Products,Kelompok,Products,Brand

class KelompokAdmin(admin.ModelAdmin):
    list_display= ('kelompok','nama_perent')
admin.site.register(Kelompok,KelompokAdmin)

class Jenis_ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','kel','nama','cu')
admin.site.register(Jenis_Products,Jenis_ProductsAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display=('id','nama')
admin.site.register(Brand,BrandAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','prod','harga_beli','harga_jual','qt')
admin.site.register(Products,ProductsAdmin)
