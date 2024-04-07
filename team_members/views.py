
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Member


class ListView(generic.ListView):
    model = Member
    paginate_by = 3
    template_name = "team_members/index.html"
    context_object_name = "members_list"

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['members_total_count'] = Member.objects.count()
        return context


class CreateView(generic.CreateView):
    model = Member
    fields = ["first_name", "last_name", "email", "phone_number", "role"]
    template_name = "team_members/add.html"
    success_url = reverse_lazy('team_members:index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['member_role_choices'] = Member.Role.choices
        return context


class EditMemberView(generic.UpdateView):
    model = Member
    fields = ["first_name", "last_name", "email", "phone_number", "role"]
    template_name = "team_members/edit.html"
    success_url = reverse_lazy('team_members:index')

    def get_context_data(self, **kwargs):
        context = super(EditMemberView, self).get_context_data(**kwargs)
        context['member_role_choices'] = Member.Role.choices
        return context


class DeleteMemberView(generic.DeleteView):
    model = Member
    success_url = reverse_lazy('team_members:index')
