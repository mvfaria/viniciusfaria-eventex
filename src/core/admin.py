# coding: utf-8
__author__ = 'viniciusfaria'

from django.contrib import admin
from .models import Speaker, Contact, Media, Talk


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ]
    prepopulated_fields = {'slug': ('name', )}


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title','description','start_time')
    inlines = [MediaInline,]


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
