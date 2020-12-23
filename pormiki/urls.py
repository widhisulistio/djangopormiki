from django.contrib import admin
from django.urls import path
from pormikidiy.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anggota', anggota, name='anggota'),
    path('tambah-anggota', tambah_anggota, name='tambah_anggota'),
    path('anggota/ubah/<int:id_anggota>', ubah_anggota, name='ubah_anggota'),
    path('anggota/hapus/<int:id_anggota>', hapus_anggota, name='hapus_anggota'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup', signup, name='signup'),
    path('export/xls', export_xls, name='export_xls'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
