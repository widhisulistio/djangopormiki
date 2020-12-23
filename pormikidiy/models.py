from django.db import models

# Create your models here.


class Dpc (models.Model):
    namadpc = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.namadpc


class Anggota (models.Model):
    no_anggota = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)
    nik = models.CharField(max_length=16)
    alamat = models.CharField(max_length=200)
    instansi = models.CharField(max_length=50)
    dpc_id = models.ForeignKey(Dpc, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to='cover/', null=True)
    tanggal = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        # return self.no_anggota + ' ' + self.nama
        return self.no_anggota
