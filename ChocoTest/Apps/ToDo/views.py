from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Стартовая страница"""
    template_name = 'index.html'
