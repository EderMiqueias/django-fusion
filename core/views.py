from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Contribuinte, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['contribuintes'] = Contribuinte.objects.order_by('?').all()

        aux = len(Feature.objects.all()) // 2
        context['featuresL'] = insert_times_list(Feature.objects.order_by('?').all()[:aux])
        context['featuresR'] = insert_times_list(Feature.objects.order_by('?').all()[aux:])
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "E-mail enviado com sucesso.")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


def insert_times_list(lin) -> list:
    lout = list()
    for x in range(len(lin)):
        lout.append((lin[x], float('%g' % (0.3*(x+1)))))
    return lout
