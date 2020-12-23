from django.shortcuts import render, redirect, HttpResponse
from pormikidiy.models import Anggota
from pormikidiy.forms import FormAnggota
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from pormikidiy.resource import AnggotaResource
# Create your views here.


def export_xls(request):
    anggota = AnggotaResource()
    dataset = anggota.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="lap anggota.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat")
            return redirect('signup')
        else:
            messages.success(request, "Terjadi kesalahan")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form': form,
        }
    return render(request, 'signup.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def hapus_anggota(request, id_anggota):
    anggota = Anggota.objects.filter(id=id_anggota)
    anggota.delete()

    messages.success(request, "Data Berhasil Dihapus")

    return redirect('anggota')


@login_required(login_url=settings.LOGIN_URL)
def ubah_anggota(request, id_anggota):
    anggota = Anggota.objects.get(id=id_anggota)
    template = 'ubah-anggota.html'
    if request.POST:
        form = FormAnggota(request.POST, request.FILES, instance=anggota)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui")
            return redirect('ubah_anggota', id_anggota=id_anggota)
    else:
        form = FormAnggota(instance=anggota)
        konteks = {
            'form': form,
            'anggota': anggota,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def anggota(request):
    anggotas = Anggota.objects.all()
    konteks = {
        'anggot': anggotas,
    }
    return render(request, 'anggota.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_anggota(request):
    if request.POST:
        form = FormAnggota(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormAnggota()
            pesan = "Data Berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-anggota.html', konteks)
    else:
        form = FormAnggota()

        konteks = {
            'form': form,
        }

        return render(request, 'tambah-anggota.html', konteks)
