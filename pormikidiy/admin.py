from django.contrib import admin
from pormikidiy.models import Anggota, Dpc

# Register your models here.


class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['no_anggota', 'nama', 'instansi', 'dpc_id']
    search_fields = ['no_anggota', 'nama', 'instansi']
    list_filter = ['dpc_id']
    list_per_page = 4


admin.site.register(Anggota, AnggotaAdmin)
admin.site.register(Dpc)
