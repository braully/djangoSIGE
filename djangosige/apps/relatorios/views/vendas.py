from SGEO.apps.vendas.models import PedidoVenda
from SGEO.apps.relatorios.tables import VendasTable
from SGEO.apps.base.custom_views import CustomListView
from django_tables2.export.views import ExportMixin
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport
from django_filters.views import FilterView


class RelatorioVendasView(ExportMixin, CustomListView):
    template_name = 'relatorios/vendas/geral.html'
    model = PedidoVenda
    table_class = VendasTable
    context_object_name = 'all_vendas'
    permission_codename = 'acessar_relatorio_vendas'

    def get_context_data(self, **kwargs):
        context = super(RelatorioVendasView,
                        self).get_context_data(**kwargs)
        context['title_complete'] = 'Relatório de Vendas'

        table = self.table_class(self.model.objects.all())
        table.paginate(page=self.request.GET.get('page', 1), per_page=15)
        table.exclude = ('lancamento_ptr')

        context['table'] = table
        RequestConfig(self.request).configure(table) #ordena

        export_format = self.request.GET.get('_export', None)
        if TableExport.is_valid_format(export_format):
            exporter = TableExport(export_format, table)
            return exporter.response('File_Name.{}'.format(export_format))

        return context