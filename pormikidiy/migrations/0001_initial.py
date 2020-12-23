# Generated by Django 2.2.12 on 2020-12-23 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dpc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namadpc', models.CharField(max_length=50)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_anggota', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
                ('nik', models.CharField(max_length=16)),
                ('alamat', models.CharField(max_length=200)),
                ('instansi', models.CharField(max_length=50)),
                ('cover', models.ImageField(null=True, upload_to='cover/')),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('dpc_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pormikidiy.Dpc')),
            ],
        ),
    ]
