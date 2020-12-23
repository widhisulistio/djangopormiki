from import_export import resources
from pormikidiy.models import Anggota
from import_export.fields import Field


class AnggotaResource(resources.ModelResource):
    dpc_id__namadpc = Field(attribute='dpc_id', column_name='dpc')

    class Meta:
        model = Anggota
        fields = ['no_anggota', 'nama', 'instansi', 'dpc_id__namadpc']
        export_order = ['no_anggota', 'nama', 'instansi', 'dpc_id__namadpc']
