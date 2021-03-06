from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from core.mixins import ProfileRequiredMixin

from .utils import find_users


class IndexPage(ProfileRequiredMixin, generic.TemplateView):
    template_name = 'discovery/index.html'

