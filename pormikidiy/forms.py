from django.forms import ModelForm
from django import forms
from pormikidiy.models import Anggota


class FormAnggota(ModelForm):
    class Meta:
        model = Anggota
        fields = '__all__'
        #fields = ['no_anggota', 'nama', 'dpc_id']
        #exclude = ['dpc_id']

        widgets = {
            'no_anggota': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'nik': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.Textarea({'class': 'form-control'}),
            'instansi': forms.TextInput({'class': 'form-control'}),
            'dpc_id': forms.Select({'class': 'form-control'}),

        }
